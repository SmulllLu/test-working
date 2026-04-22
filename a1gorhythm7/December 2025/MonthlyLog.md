# December 2025

## Pull #303 https://github.com/ruyisdk/ruyisdk-website/pull/303
- Unify content width across homepage, about, news, community, and statistics pages using a shared CSS variable and utility class.
- Refine news page layout and article structure for clearer two-column display and better visual hierarchy on wide screens.

## Pull #304 https://github.com/ruyisdk/ruyisdk-website/pull/304
- Refactor the About page to use localized MDX files for English, Chinese, and German.
- Localize page title and remove top logo/title block.
- Streamline About page header, keep sidebar and overall layout.

## Pull #305 https://github.com/ruyisdk/ruyisdk-website/pull/305
- Standardize and localize biweekly news titles in English, German, Chinese.
- Add skeleton loading components and styles for news page and sidebar cards.
- Remove RuyiSDK brand from biweekly sections, add tests for title localization.

## Pull #310 https://github.com/ruyisdk/ruyisdk-website/pull/310 (draft, closed)
- Add a new /downloads page with architecture-aware downloads for RuyiSDK package manager and IDE.
- Generate package manager metadata during build; provide local stub for offline builds.
- Update navigation and docs links to use new /downloads route.
- Theming enhancements: introduce new colors and reusable styles for downloads.

## Pull #311 https://github.com/ruyisdk/ruyisdk-website/pull/311
- Finalize new /downloads page with architecture selection and install guidance.
- Fetch latest package manager release metadata from remote API at build time.
- Automate contributor and release metadata refresh for development workflow.

## Pull #312 https://github.com/ruyisdk/ruyisdk-website/pull/312
- Prevent CI deadlock by relaxing diff check for generated_contributors.json, logging changes instead of failing jobs.
- Update CI workflow to only report differences when commit counts change due to new commits.

## Pull #314 https://github.com/ruyisdk/ruyisdk-website/pull/314
- Simplify package manager and IDE download hints, use generic link guidance.
- Improve /downloads IDE card layout with flex row and download icon.