# Tauseef Khan — portfolio

Everything in this folder is the site. There is no build step: what you push is what gets served.

    index.html                              the whole site: home, six case studies, project pop-ups, styles, scripts
    Tauseef_Khan_Product_Designer_CV.pdf    the CV every "Download CV" / "CV" button points to
    og.png                                  link-preview image (LinkedIn, Slack, iMessage, X)
    favicon.svg                             tab icon (the TK. tile; index.html carries the same icon inline)
    images/projects/                        pictures for the More projects cards and pop-ups
    images/NAMES.txt                        file names for the case-study image slots and the tool logos
    images/tools/                           tool logos for the Tools panel (optional)
    images/portrait.webp                    your photo in the hero
    robots.txt                              lets search engines index the site
    netlify.toml                            caching + security headers (Netlify reads it; harmless elsewhere)
    .nojekyll                               tells GitHub Pages to serve the folder as it is
    download-images.py                      optional helper, see step 5
    sitemap.xml                             the page list for search engines

**New in this version (14 Oct 2026).** Replace every file in the repository with the files in this zip (same folders), then commit and push.
- New look: a deeper dark theme (still the default), with a pink → coral → violet gradient used sparingly — the name, the portrait ring, the scroll cue, the reading-progress bar and the hover edges. Orange stays the accent colour. Softer outlines, and a gentle glow on hover instead of hard shadows.
- Hero: name, role, positioning line, the portrait with a dot that circles it (it pauses on hover) and a SCROLL cue on the right.
- Top bar: the TK. logo in Space Grotesk, section links with a dot under the current section, CV and "Let's talk". A gradient reading-progress line runs across the top as you scroll.
- Tab icon: a TK. tile that switches with light and dark mode (favicon.svg holds the same icon). og.png, the link-preview image, is redrawn in the new look — LinkedIn keeps old previews for a while; paste the link into LinkedIn's Post Inspector to refresh it.
- Experience is grouped by project. ZoomRx now reads "Hybrid, India".
- Tools I work with: five groups by stage of the work. A tool shows its logo once its file is in images/tools/ and listed in `SITE.toolLogos` (step 4; file names in images/NAMES.txt); until then it is a plain label.
- MR Survey App: rebuilt around its research — primer, the study, what the research said, who it was for, the decisions, directions rejected, validation and measurement — with a four-row 10-second summary. The NPS story is corrected: the measurement system was built first (an Excel sheet, later a dashboard built with AI) and −8 was its first reading.
- Each case study's project link now sits next to its title.
- Fixes: the More projects hover shadow is no longer cut off, and the MR Survey App "All work / Next" buttons no longer show up on the home page.

**Removed in this version.** Delete these from the repository if they are still there: the `ar/` folder and the `fonts/` folder. The site is English only now.

## 1. Publishing
Commit and push. If the repository is connected to Netlify or GitHub Pages, the push publishes the site.
(Without a connected repository: app.netlify.com → Add new site → Deploy manually → drop this folder.)

## 2. SEO: what is done, and what needs the site address
Done in index.html: page title and description, one main heading, heading order, link-preview tags, structured data (who you are, your role, your profiles), image alt text, and a robots rule that allows indexing.

The site address is already in place: canonical link, link-preview addresses, sitemap.xml and the Sitemap line in robots.txt all use
https://tauseefkhan095-gif.github.io/tauseefkhan.pd. If the address changes, replace it in index.html, sitemap.xml and robots.txt.

One GitHub Pages detail: when the site lives in a sub-folder of github.io, search engines do not read this robots.txt (they only look at the root of the host). Nothing is blocked either way; submit sitemap.xml in Search Console so it is found.

After the site is live, add it in Google Search Console and submit the address (or the sitemap).

## 3. The note form
"Send" posts the name and purpose to FormSubmit, which forwards them to tauseefkhan095@gmail.com. The first note sent from the live site triggers an activation email from FormSubmit: click the link in it once (check spam). Until then, and whenever the service cannot be reached, the visitor's email app opens with the note filled in instead.
To change where notes go, edit `formEndpoint` in the SITE settings (step 4).

## 4. Settings
Near the top of the script in index.html there is a block called `SITE`:
- `images`: file names you have added to images/ (see images/NAMES.txt).
- `toolLogos`: logo files you have added to images/tools/ for the Tools panel, e.g. `['figma.svg','v0.svg']`.
- `findImages`: `true` makes the site look for every image slot by itself while you are placing pictures. Switch it off for launch.
- `hideEmpty`: `true` hides image slots and quote slots that are still empty.
- `quotes`: testimonials and pull quotes.
- `formEndpoint`: where the note form is delivered.

Light or dark on first visit: `DEFAULT_THEME` in the first `<script>` at the top of index.html. Visitors who switch keep their own choice.

## 5. Pictures
- Stored in this folder (images/projects/): the MR Survey App cover, and the pictures for Clear.bio, EFL Clik, ASAPP, World Class Health and MaxSold.
- Loaded from other servers: sixteen projects take their pictures from the old Framer portfolio, and Click it by Holcim takes its cover and screen pictures from clickitapp.io. They show as long as those servers keep them. To make the site independent of them, run this once in this folder, then commit the result:

      python3 download-images.py

  It saves every such picture into images/projects/ and updates index.html to use the local copies.
- Case studies: every case study has marked places for pictures. They stay hidden on the live site until a picture is added. Name files as in images/NAMES.txt, put them in images/, and list them in `SITE.images`.

## 6. Certificates
The Google UX and Interaction Design Foundation cards link to their certificates and show how many certifications each issuer has awarded you (8 and 14). To change an address or a total, search index.html for `cert-row`.
To give another education card a link, put this inside the card, after its last line of text:
`<div class="cert-row"><a class="cert" href="CERTIFICATE-ADDRESS" target="_blank" rel="noopener noreferrer">View certificate <span aria-hidden="true">↗</span></a></div>`

## 7. Editing text
All text lives in index.html. A new CV replaces the PDF under the same file name.
