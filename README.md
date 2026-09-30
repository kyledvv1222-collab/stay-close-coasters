# Stay Close Coasters

A mobile web app of PFLAG NYC's **Stay Close** conversation-starter coasters. Parents, families and LGBTQ+ people can shuffle a coaster, browse by deck (Shared, Loved One, LGBTQ+), save favorites, add notes and track the conversations they've had.

**Live app:** https://kyledvv1222-collab.github.io/stay-close-coasters/

Open it on a phone, then use Share → Add to Home Screen (iPhone) or ⋮ → Add to Home screen (Android) to install it with the PFLAG NYC icon.

## Files
- `index.html` — the app (built from `src/app.html`)
- `src/app.html` — single source for the app, also published as the Claude Artifact preview
- `manifest.webmanifest`, `icons/` — home screen name and icons
- `sw.js` — offline support after the first visit
- `build.py` — run `python3 build.py` after editing `src/app.html`

Saved coasters, notes and progress stay on each person's device. There are no accounts and no data leaves the phone.
