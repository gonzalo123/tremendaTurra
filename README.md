# Tremenda Turra

A small static essay site for Gonzalo Ayuso, built with Pelican, Python, Markdown, and GitHub Pages.

The site is meant for long-form essays in Spanish about ancient Greece, tragedy, art, philosophy, mythology, and pop culture. It is not a technical blog, a portfolio, or a web app. The reader-facing site is plain static HTML and CSS, public, and requires no login.

## Why Pelican

Pelican keeps the publishing workflow simple: write Markdown files, run a build, and publish the generated `output/` directory. It is Python-based, does not require Jekyll, and works well with GitHub Pages through GitHub Actions.

## Local Setup

```bash
make install
```

This creates a local `.venv/` virtual environment and installs the dependencies from `requirements.txt`.

## Create a New Essay

```bash
make new TITLE="Mi nuevo ensayo"
```

The command creates a draft Markdown file in `content/articles/` with Pelican metadata already filled in. Publishing is intentionally boring: the author only needs to write Markdown files in `content/articles/`.

## Preview Locally

```bash
make serve
```

The site will be available at:

```text
http://localhost:8000
```

## Build for Production

```bash
make build
```

Production HTML is generated into `output/`.

## Deploy to GitHub Pages

The GitHub Actions workflow in `.github/workflows/pages.yml` builds and deploys the site when changes are pushed to the `main` branch. It can also be run manually from the Actions tab.

In the repository settings, configure GitHub Pages to use GitHub Actions as the source.

## Project Layout

```text
content/articles/   Markdown essays
content/pages/      Simple standalone pages
content/images/     Static image files
theme/el-canto/     Local Pelican theme
output/             Generated site, not committed
```

No analytics, comments, external fonts, CSS frameworks, JavaScript, databases, CMS, Node, Docker, or build pipeline beyond Pelican are used.
