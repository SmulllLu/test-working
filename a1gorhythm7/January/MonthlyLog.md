# January 2026

## News & fixes for the website

### Pull #326 https://github.com/ruyisdk/ruyisdk-website/pull/326
- Fix layout issues when news pictures have different height/width ratios.
- Adjust article and skeleton layouts so text and thumbnails stretch consistently across aspect ratios.
- Add a `check-news-images` validation script for news image existence and basic size/aspect constraints.
- Wire the image validation script into package.json for optional strict checking.

### Pull #329 https://github.com/ruyisdk/ruyisdk-website/pull/329
- Optimize the mobile news page: refine typography, title/date/summary layout for better small-screen readability.
- Ensure article images render as block elements while keeping existing hover scaling behavior.
- Improve responsive behavior of news cards to reduce layout shifts on narrow viewports.

### Pull #330 https://github.com/ruyisdk/ruyisdk-website/pull/330
- Improve the subscribe form and button with consistent, responsive layout and localized copy.
- Add internationalization support for labels, placeholders, and status messages.
- Refresh visual design (gradients, shadows, focus/hover states) and replace inline styles with CSS module classes for maintainability and consistent layout across viewports.

### Pull #331 https://github.com/ruyisdk/ruyisdk-website/pull/331
- CI behaviour fix for contributor JSON file: add a CI step to detect changes to the generated contributors JSON and only run the diff check when that file changed.
- Prevent unnecessary CI failures by skipping the generated_contributors.json diff check when no relevant generation changes exist.


### Pull #341 https://github.com/ruyisdk/ruyisdk-website/pull/341
- Add a richer downloads experience with direct architecture-aware links and thank-you redirect.
- Switch to a fast mirror as the primary source for package manager releases.
- Introduce an internal slide deck at `/slide` for the website revamp with keyboard navigation and local route previewing.
- Downloads selector includes CPU architecture detection, source/architecture choice, and localized thank-you redirection.
- Metadata enhancements: scrape the fast mirror for latest packages, synthesize per-architecture URLs, and improve fallbacks and robustness.
- Update localized documentation to support the new downloads flow and labels.

### Pull #343 https://github.com/ruyisdk/ruyisdk-website/pull/343
- Extract shared UI elements into reusable components under the `common` directory.
- Introduce the `PageBackground` component, unify card/avatars/statistics icon layouts.
- Refactor contributors, about, and news pages to consume these shared components.
- Export new shared components for site-wide usage.

### Pull #344 https://github.com/ruyisdk/ruyisdk-website/pull/344
- Migrate the site styling pipeline from UnoCSS to Tailwind CSS.
- Configure Tailwind CSS and Autoprefixer as part of the Docusaurus and PostCSS build.
- Unify color, typography, layout, and shadow settings with a shared Tailwind configuration.
- Replace UnoCSS plugin and stylesheet with Tailwind equivalents, integrate with existing Sass styles.
- Update package dependencies and build processes accordingly.
