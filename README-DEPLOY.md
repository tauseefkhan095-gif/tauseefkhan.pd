# Tauseef Khan — portfolio

Everything in this folder is the site. There is no build step: what you push is what gets served.

    index.html                              the whole site: home, six case studies, project pop-ups, styles, scripts
    Tauseef_Khan_Product_Designer_CV.pdf    the CV every "Download CV" / "CV" button points to
    og.png                                  link-preview image (LinkedIn, Slack, iMessage, X)
    favicon.svg                             tab icon
    images/projects/                        pictures for the More projects cards and pop-ups
    images/NAMES.txt                        file names for the case-study image slots
    robots.txt                              lets search engines index the site
    netlify.toml                            caching + security headers (Netlify reads it; harmless elsewhere)
    .nojekyll                               tells GitHub Pages to serve the folder as it is
    download-images.py                      optional helper, see step 5
    sitemap.xml                             the page list for search engines

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
- `findImages`: `true` makes the site look for every image slot by itself while you are placing pictures. Switch it off for launch.
- `hideEmpty`: `true` hides image slots and quote slots that are still empty.
- `quotes`: testimonials and pull quotes.
- `formEndpoint`: where the note form is delivered.

Light or dark on first visit: `DEFAULT_THEME` in the first `<script>` at the top of index.html. Visitors who switch keep their own choice.

## 5. Pictures
- More projects: ASAPP, Holcim Click-it, World Class Health and MaxSold use the files in images/projects/.
- The other project pictures (Voohoo Live, Fundoo-Learning and the fifteen projects added from the old portfolio) still load from the old Framer portfolio's image server. They show as long as that server keeps them. To make the site independent of it, run this once in this folder, then commit the result:

      python3 download-images.py

  It saves every such picture into images/projects/ and updates index.html to use the local copies.
- Case studies: name files as in images/NAMES.txt, put them in images/, and list them in `SITE.images`.

## 6. Certificates
The education cards are ready for certificate links. To add one, put this line inside the card, after its last line of text:
`<a class="cert" href="CERTIFICATE-ADDRESS" target="_blank" rel="noopener noreferrer">View certificate <span aria-hidden="true">↗</span></a>`

## 7. Editing text
All text lives in index.html. A new CV replaces the PDF under the same file name.
