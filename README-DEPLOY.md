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

**New in this version (15 Oct 2026).** Replace every file in the repository with the files in this zip (same folders), then commit and push. Everything from the 14 Oct version is still in, plus:
- No em dashes anywhere in the site's text, diagrams, alt text or project pop-ups. Date ranges use an en dash (NOV 2022 – PRESENT).
- MR Survey App: the survey-loop diagram's four cards have more room at the bottom. Two screen recordings, as GIFs: Patient Load before and after (Decision 2) and Zena, the support agent (Decision 1).
- Zena in More projects: a cover picture, the recording, and a quick case study in its pop-up.
- Gribb Tech: rebuilt around its two audiences, with its own structure (two seats, one engine; every decision told from the manager's and the driver's seat; what we didn't build; user flows for the driver app and the client dashboard; one closing results section) and eight screens placed in the insights, the decisions and Experience Design.
- Every case study: the project link sits at the right of the title row; the Research & Evidence block reads as rows.
- New files in images/projects/: survey-patient-load.gif, zena-in-action.gif, card-zena.webp, and gribb-insight-1/2/3, gribb-decision-2/4, gribb-shift-checkin, gribb-shift-damage, gribb-dash-checkin (.webp). The GIFs are large (10 MB and 15 MB); they load only when someone opens that case or pop-up.

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
