Ruyiinlive component update (#426)
This PR updates the RuyiInLive homepage component to fetch and display new community statistics and hot tags. It introduces the display of 30-day activity metrics (active users, posts, topics) and a pill-based list of popular Ruyi SDK tags, powered by a newly generated hot-tags API. The data fetching logic is simplified by consuming the public statistics endpoint, and the layout for metrics and tags is made more responsive. Additionally, it adds a CI script to periodically generate the hot-tags data used in the site, improving maintainability through automation.

Downloads page refactor (#418)
This PR significantly refactors the downloads page, separating the IDE integrations into distinct VS Code and Eclipse sections with their own styling and branding. Each extension now has a dedicated section featuring titles, descriptions, and logos. Anchor IDs are added for improved navigation. The layout, typography, and header gradients are refreshed to improve clarity and visual hierarchy, and the package manager card is updated with a new logo and a link to the IDE mirror, resulting in a more visually appealing and user-friendly downloads page.

Fix height calculation in /about page (#408)
This PR simplifies the /about page layout by removing JavaScript references and resize listeners that were previously required to manually sync the partners section height with the main content. These changes streamline the page code, reduce complexity, and eliminate unnecessary logic previously used for layout alignment.

Index news three cards layout (#407)
The NewsShowcase component is simplified in this PR to present up to three news items in a static three-card grid on desktop and a vertical list on mobile. Auto-rotation and visibility logic are removed in favor of a direct static rendering of the latest news items based on fetched data. This makes the news section easier to maintain and provides a consistent visual layout across devices.

Refactor about page (#396)
This PR extensively refactors the About page, shifting from MDX components to locale-specific Markdown files for loading About, contact, and QR code content, greatly improving content management and localization. A reusable partners section is created and integrated into both About and Community pages, presenting an expanded list of partner logos. The PR standardizes QR code images and introduces a community navigation dropdown for easier site exploration. Styling for Markdown content is also enhanced through new CSS modules for better visual consistency.

Add issue data in contributors page (issue #307) (#395)
This PR adds an issue count metric to the contributors page, updating static GitHub API data files to include these statistics. The contributors page now displays total issues alongside contributors, commits, and pull requests. The code also gracefully defaults to fallback totals if issue data is missing for any repository and updates translations for the new statistics label, enhancing the accuracy and completeness of contributor analytics.

Disable dark mode for CodeBlock (#383)
This PR enforces a light theme appearance for the documentation CodeBlock component, overriding any global dark mode. It removes all dark mode-specific Tailwind CSS classes from the CodeBlock container and forces line highlighting to use the light theme. This standardization ensures that code snippets remain clear and readable regardless of site theme settings.
