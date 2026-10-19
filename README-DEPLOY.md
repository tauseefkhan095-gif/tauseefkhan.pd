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

**New in this version (20 Oct 2026).** Replace every file in the repository with this zip's files, then commit and push. Since 19 Oct:
- MR Survey App: NPS on real data (−13 in Nov 2024 to +44 by early 2026, chart redrawn from the Panel Health dashboard); 30,000+ responses credited to the NPS question and end-of-survey feedback together; the Panel Health dashboard as a three-screen carousel; four quotes with names; promoters/passives/detractors in the vocabulary; a live, interactive design system in section 07; Go to app and Go to website links; the SUS paragraph in plain words; panel 60K+.
- Numbers in paragraphs are semibold (case studies and More-projects pop-ups).
- Gribb Tech: 18 months; the CEO beside the CTO; Moove and Netradyne linked.
- Bentley Mulliner: a Sources list; the empty render placeholder removed.
- Ferma: named as Ferma Chat, now Ferma Agents. More projects: Media Tracking rebuilt; Curie.md line added.
- New images in images/projects/: survey-nps-trend, survey-nps-table, survey-nps-surveys.

**New in the 19 Oct version.** og.png, the picture that WhatsApp, LinkedIn and iMessage show when the link is shared, is redrawn with the new portrait (it still carried the old one). The page's og:image and twitter:image URLs now end in `?v=20261019`, so the apps fetch the new file instead of their cached copy; a message sent after this version is live shows the new card (a preview already sitting in an old chat does not update). sitemap.xml lastmod 2026-10-19. Everything below is unchanged from the 18 Oct version.

**New in the 18 Oct version.** Replace every file in the repository with the files in this zip (same folders), then commit and push. New file: `ask-index.json` at the top level, next to index.html. It is what the "Ask me" box answers from; without it the box says it could not load its notes. Everything from the 16 Oct version is still in, plus:
- "Ask me": a small floating button, bottom right, that answers a visitor's question with the part of the site that covers it (no server, nothing typed leaves the browser). The optional AI version is in the toolchain folder of the backup, not here.
- More-projects pop-ups are wider (80% of the screen), the live-project link sits on the title row, and the goal and decision cards run full width.
- Curie.md (More projects): the cover composite on the card, the sign-in composite in the pop-up, a new Curie Games section with a six-screen carousel. Eight new pictures in images/projects/ (card-curie, curie-signin, curie-games-1..6).
- A new hero portrait (images/portrait.webp; it is embedded in index.html, the file is kept for reference).
- Click it by Holcim: his cover composite on the card (images/projects/card-click-it-holcim.webp, replaced); the card no longer fetches a picture from clickitapp.io.
- Amaze Mobility: the pop-up rewritten from the agency's published case study (facts, concept, features, process; it states no results, so none are claimed) with his three pictures (card-amaze, amaze-screens, amaze-flow in images/projects/).
- Raftaarr: rebuilt from the agency's case study with a style guide built in CSS, and your three pictures (card-raftaarr, raftaarr-screens, raftaarr-web); nothing loads from Framer for it any more.
- Click it by Holcim: rebuilt from the agency's case study and clickitapp.io, with a CSS style guide and your pictures (card-click-it-holcim replaced at 1600px, holcim-screens, holcim-trio, holcim-f-home / -cart / -settlement / -help / -track / -users); holcim-click-it-g1/g2 are gone, and nothing loads from clickitapp.io any more.
- EFL Clik: rebuilt from the agency's case study and EFL's blog, with a CSS style guide and your pictures (efl-cover and efl-multi replaced at higher resolution; efl-d-profile / -loan / -eligible recut; new efl-d-welcome, efl-d-credit, efl-d-more).
- Ferma Congress and GoCar Share removed from More projects; the remaining 29 are in your order (Amaze first, Yaye last).
- Ferma.AI rebuilt with its own structure (anatomy of an answer, the decision log, beyond the chat) and your screens, a new home-page cover, and its design system designed on the page at the end.
- Boilerplate Generator rebuilt from the project files: two reversals, the eight canonical screens, screen to rule, the full architecture, one real run start to finish, the output folder and three real outputs rendered live, and the efficiency outcome (three teams and ~7 days → the SPI team alone, ~1 hour). New home-page cover.
- More projects: Safura AI is now PAIA (Personal Artificial Intelligence App).
- New files in images/projects/: cover-ferma (replaced), cover-bpg, ferma-01 (replaced), ferma-03, ferma-04 (replaced), ferma-anatomy, ferma-narrow, ferma-focus, ferma-focus-manage, ferma-07, ferma-signin, ferma-mobile, bpg-scr-* (8), bpg-ill-* (3), bpg-derive-screen, bpg-run-1..5.

**New in the 16 Oct version.** Replace every file in the repository with the files in this zip (same folders), then commit and push. Everything from the 15 Oct version is still in, plus:
- Sagan.AI rebuilt with its own structure: the interview as a script (V2's arc, line by line), four versions to get here (the developers' base, V1, V2, each with a carousel of your screens on web and on mobile), the revenue outcome (from zero to about $2M a year), and a closing section with the Sagan Agents style guide designed on the page (logo form, wordmark, palette, type, icons).
- Sagan.AI images: a new card cover on the home page, a new first image in the case, and 49 screens in images/projects/ (sagan-01, -02, -04, sagan-v0-01..04, sagan-v1-w-01..09, sagan-v1-m-01..09, sagan-v2-w-01..11, sagan-v2-m-01..12, cover-sagan).
- Carousels: a slide only appears when its picture exists; fast clicks on the arrows advance correctly.

**New in the 15 Oct version.** Everything from the 14 Oct version is still in, plus:
- No em dashes anywhere in the site's text, diagrams, alt text or project pop-ups. Date ranges use an en dash (NOV 2022 – PRESENT).
- MR Survey App: the survey-loop diagram's four cards have more room at the bottom. Two screen recordings, as GIFs: Patient Load before and after (Decision 2) and Zena, the support agent (Decision 1).
- Zena in More projects: a cover picture, the recording, and a quick case study in its pop-up.
- Gribb Tech: rebuilt around its two audiences, with its own structure (two seats, one engine; every decision told from the manager's and the driver's seat; what we didn't build; user flows for the driver app and the client dashboard; one closing results section) and eight screens placed in the insights, the decisions and Experience Design.
- Every case study: the project link sits at the right of the title row; the Research & Evidence block reads as rows.
- Gribb Tech: a new section on the rebrand, with the style guide designed on the page (logo on purple, white and black, palette, Montserrat, brand mark).
- Bentley Mulliner: a new cover (card and case), a carousel of seven iPad screens in session order with arrows, and an iPad + iPhone pair; also rebuilt with its own structure (three people around one iPad; the no-3D technique in its own section; every decision as before and after; a user flow of the configurator; what we removed; what changed and what I can't claim).
- New files in images/projects/: survey-patient-load.gif, zena-in-action.gif, card-zena.webp, gribb-insight-1/2/3, gribb-decision-2/4, gribb-shift-checkin, gribb-shift-damage, gribb-dash-checkin, bentley-flow-01 to 07, bentley-showcase-tablet and bentley-showcase-mobile (.webp); cover-bentley.webp is replaced. The GIFs are large (10 MB and 15 MB); they load only when someone opens that case or pop-up.

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
