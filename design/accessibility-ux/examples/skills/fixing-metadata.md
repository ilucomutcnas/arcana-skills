# Fixing Metadata — Examples

## Essential Page Metadata

```html
<head>
  <title>Product Name — Page Title | Brand</title>
  <meta name="description" content="Concise 150-160 character description of this page content." />
  <link rel="canonical" href="https://example.com/page" />
  <meta name="robots" content="index, follow" />
  <html lang="en">
</head>
```

## Open Graph Tags

```html
<meta property="og:title" content="Page Title | Brand" />
<meta property="og:description" content="Description matching meta description." />
<meta property="og:url" content="https://example.com/page" />
<meta property="og:image" content="https://example.com/og-image.jpg" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Brand Name" />
```

## Twitter Card Tags

```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="Page Title" />
<meta name="twitter:description" content="Short description." />
<meta name="twitter:image" content="https://example.com/twitter-image.jpg" />
```

## JSON-LD Structured Data

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Page Title",
  "description": "Page description.",
  "url": "https://example.com/page"
}
</script>
```

## Audit Workflow

1. Identify pages with missing or incorrect metadata.
2. Fix critical issues first (duplicates, indexing).
3. Ensure title, description, canonical, and og:url agree.
4. Verify social cards render on a real URL, not localhost.
5. Keep diffs scoped to metadata only.
