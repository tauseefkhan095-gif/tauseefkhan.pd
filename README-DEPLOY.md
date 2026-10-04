# Deploying the portfolio

What's in this folder is the complete site. Nothing else is needed.

    index.html                              the whole site in English (all case studies, styles, scripts)
    ar/index.html                           the same site in Arabic (right-to-left), served at /ar/
    fonts/                                  the Arabic typefaces the Arabic page uses
    Tauseef_Khan_Product_Designer_CV.pdf    the CV every "Download CV" / "CV ↓" control points to
    og.png                                  link-preview image (Slack, LinkedIn, iMessage, X)
    favicon.svg                             tab icon
    images/                                 drop your screenshots here — see images/NAMES.txt for the exact file names
    netlify.toml                            caching + security headers (Netlify reads it automatically; harmless elsewhere)
    robots.txt                              lets search engines index the site

Keep these files together: index.html links to the CV, the icon and the images by name.

## 1. Put it online (Netlify, free)
1. Go to app.netlify.com → "Add new site" → "Deploy manually".
2. Drag this whole folder (or the zip) onto the drop zone. The site is live on a netlify.app address in ~20 seconds.
3. Every later update: same drag-and-drop onto the site's "Deploys" tab.

## 2. Your own domain
Buy the domain (Namecheap / GoDaddy / Google Domains), then in Netlify: Domain management → Add custom domain → follow the DNS steps shown. HTTPS is automatic.

## 3. One edit after you know the domain
In index.html, change both `content="og.png"` values (og:image and twitter:image) to the full address, e.g. `https://tauseefkhan.design/og.png`. Link previews only work with a full URL. Do the same in ar/index.html (there the value is `../og.png`).

In both files, also make the three `hreflang` links near the top absolute: `https://yourdomain/` for English and x-default, `https://yourdomain/ar/` for Arabic. They tell search engines the two pages are the same site in two languages.

## 4. Filling the site
- Images: name files exactly as in images/NAMES.txt (webp, png or jpg), drop them into images/, and add each file name to `SITE.images` near the top of the script in index.html, e.g. `images:['sagan-01.webp','mock-gribb.png']`. Captions appear under them automatically.
- While you're still placing images, `SITE.findImages:true` makes the site look for every slot by itself, no list needed. Turn it back off for launch: with it on, every empty slot costs visitors a few failed requests.
- Testimonials and in-case pull quotes: edit `SITE.quotes` near the top of the script in index.html.
- `SITE.hideEmpty` (same place): `true` hides anything still unfilled (set for launch). Set `false` while you're placing images, so you can see every slot.
- Light or dark on first visit: `DEFAULT_THEME` in the first `<script>` at the top of index.html (`'light'` or `'dark'`). Visitors who switch keep their own choice.
- New CV: replace the PDF and keep the same file name.

## 5. Two languages
- English is at `/`, Arabic at `/ar/`. The switch sits in the top bar (العربية / English) and in the bar of every case study, and it opens the same view in the other language.
- The two pages are separate files. A text change in index.html needs the matching change in ar/index.html; so do the settings in step 4 (`SITE.images`, `SITE.quotes`, `DEFAULT_THEME`). Image files are shared: both pages read the same images/ folder.
- The CV is English only, and the Arabic page says so next to the download.
- The Arabic was translated by Claude and has not been reviewed by a native speaker. Have one read it before you publish, starting with the home page and your name (توصيف خان).

## 6. Editing text
The text lives in index.html. The case studies started in Notion, but this build also carries the résumé-synced edits made directly in the page, so the Notion pages are no longer an exact copy. Edit index.html, or bring Notion up to date first if you want to go back to converting from it.
