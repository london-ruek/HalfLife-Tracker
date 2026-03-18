# HalfLife — Medication Saturation Tracker

A Progressive Web App (PWA) for tracking medication saturation, hormone levels, bloodwork, and protocols using pharmacokinetic half-life modelling.

## Features

- **Pharmacokinetic curves** — real half-life decay math for all compounds
- **Hormone pooling** — ester conversion factors, free hormone tracking (Test E/C/P, Deca, Tren, etc.)
- **Steady State calculator** — 90/95/99% milestone projections with build-up charts
- **Dose Log** — timestamped history with free hormone calculations
- **Schedule** — future protocol planning with projected saturation curves
- **Bloodwork** — colour-coded results (35 built-in reference ranges + custom overrides)
- **Trend charts** — per-marker charts across all blood draws
- **Active Flags** — dashboard alerts for out-of-range markers + HCT donate warning
- **Journal** — daily notes with mood tracking and searchable tags
- **Export** — CSV download for medications and dose history
- **Dark/light mode** — preference saved locally
- **Offline** — works fully offline once installed
- **PWA** — installable on iOS and Android home screen

## Files

```
halflife-pwa/
├── index.html       ← Main app (single file)
├── manifest.json    ← PWA manifest
├── sw.js            ← Service worker (offline support)
└── icons/
    ├── icon-192.png ← App icon
    └── icon-512.png ← App icon (large)
```

## Deployment

### Option 1 — GitHub Pages (free, recommended)
1. Create a new GitHub repo (e.g. `halflife`)
2. Upload all files maintaining the folder structure
3. Go to Settings → Pages → Deploy from branch → main → / (root)
4. Your app will be live at `https://yourusername.github.io/halflife`

### Option 2 — Netlify (free, drag & drop)
1. Go to [netlify.com](https://netlify.com) and sign up free
2. Drag the entire `halflife-pwa` folder onto the deploy area
3. Done — you get a live URL instantly

### Option 3 — Vercel (free)
1. Install Vercel CLI: `npm i -g vercel`
2. Run `vercel` inside the `halflife-pwa` folder
3. Follow the prompts

### Option 4 — Local server (testing)
```bash
cd halflife-pwa
python3 -m http.server 8080
# Open http://localhost:8080
```

Note: Service workers require HTTPS in production (GitHub Pages, Netlify, and Vercel all provide this automatically).

## Installing on your phone

### Android (Chrome)
- Open the app URL in Chrome
- Tap the "Install" banner at the bottom, OR
- Tap the ⋮ menu → "Add to Home screen"

### iOS (Safari)
- Open the app URL in Safari
- Tap the Share button (square with arrow)
- Scroll down and tap "Add to Home Screen"
- Tap "Add"

The app will appear on your home screen with the HalfLife icon and run in full-screen standalone mode, just like a native app.

## Data

All data is stored locally in your browser's localStorage — it never leaves your device.
To back up your data, use the Export tab to download CSVs.

## Disclaimer

This app is for personal tracking purposes only. It is not medical advice.
Always consult a qualified healthcare provider regarding medications and protocols.
