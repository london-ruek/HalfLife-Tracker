#!/usr/bin/env python3
"""Generate PNG icons for HalfLife PWA"""
import struct, zlib, math

def make_png(size):
    """Create a simple PNG icon programmatically"""
    w, h = size, size
    
    # Build pixel data - dark background with HL logo
    pixels = []
    cx, cy = w//2, h//2
    r_outer = int(w * 0.42)
    r_inner = int(w * 0.30)
    stroke = max(2, int(w * 0.04))
    
    for y in range(h):
        row = []
        for x in range(w):
            dx, dy = x - cx, y - cy
            dist = math.sqrt(dx*dx + dy*dy)
            
            # Background
            bg = (10, 14, 23, 255)
            
            # Outer circle ring (cyan)
            if r_outer - stroke <= dist <= r_outer:
                row.extend([56, 189, 248, 255])
                continue
            
            # Inner area
            if dist < r_outer - stroke:
                # H letter (left half)
                h_w = int(w * 0.12)
                h_h = int(h * 0.30)
                h_x_left = cx - int(w * 0.22)
                h_x_right = cx - int(w * 0.04)
                h_bar_y = cy - int(h * 0.02)
                h_bar_h = int(h * 0.06)
                
                in_left_v = (h_x_left <= x <= h_x_left + h_w) and (cy - h_h <= y <= cy + h_h)
                in_right_v = (h_x_right <= x <= h_x_right + h_w) and (cy - h_h <= y <= cy + h_h)
                in_horiz = (h_x_left <= x <= h_x_right + h_w) and (h_bar_y <= y <= h_bar_y + h_bar_h)
                
                # L letter (right half)
                l_x = cx + int(w * 0.08)
                l_w = int(w * 0.11)
                l_h = int(h * 0.30)
                l_foot_h = int(h * 0.07)
                l_foot_w = int(w * 0.18)
                
                in_l_v = (l_x <= x <= l_x + l_w) and (cy - l_h <= y <= cy + l_h)
                in_l_foot = (l_x <= x <= l_x + l_foot_w) and (cy + l_h - l_foot_h <= y <= cy + l_h)
                
                if in_left_v or in_right_v or in_horiz:
                    row.extend([56, 189, 248, 255])  # cyan H
                elif in_l_v or in_l_foot:
                    row.extend([100, 116, 139, 255])  # muted L
                else:
                    row.extend(bg)
            else:
                row.extend(bg)
        
        pixels.append(row)
    
    # Encode as PNG
    def pack_chunk(chunk_type, data):
        c = chunk_type + data
        return struct.pack('>I', len(data)) + c + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    
    # IHDR
    ihdr_data = struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0)  # 8-bit RGB... actually RGBA
    ihdr_data = struct.pack('>II', w, h) + bytes([8, 6, 0, 0, 0])  # RGBA
    
    # Raw pixel data with filter bytes
    raw = b''
    for row in pixels:
        raw += b'\x00'  # filter type none
        raw += bytes(row)
    
    compressed = zlib.compress(raw, 9)
    
    png = b'\x89PNG\r\n\x1a\n'
    png += pack_chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
    png += pack_chunk(b'IDAT', compressed)
    png += pack_chunk(b'IEND', b'')
    
    return png

for size, name in [(192, 'icon-192.png'), (512, 'icon-512.png')]:
    data = make_png(size)
    with open(f'/home/claude/halflife-pwa/icons/{name}', 'wb') as f:
        f.write(data)
    print(f'Generated {name} ({len(data)} bytes)')

print('Icons generated successfully')
