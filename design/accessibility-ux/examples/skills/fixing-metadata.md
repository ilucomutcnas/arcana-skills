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

## Stage 3 Multi-Locale Product Metadata Cleanup

## Stage 3 Concrete Multi-Locale Metadata Cleanup
### Route coverage
| Locale | Route | Canonical |
|---|---|---|
| EN | `/en/products/wireless-headset` | `https://shop.example.com/en/products/wireless-headset` |
| ES | `/es/productos/auriculares-inalambricos` | `https://shop.example.com/es/productos/auriculares-inalambricos` |
| FR | `/fr/produits/casque-sans-fil` | `https://shop.example.com/fr/produits/casque-sans-fil` |

### Metadata parity table
| Field | EN | ES | FR |
|---|---|---|---|
| title | Wireless Headset - 30h Battery | Auriculares inalámbricos - batería 30 h | Casque sans fil - batterie 30 h |
| description | Over-ear headset with ANC and USB-C fast charge. | Auriculares circumaurales con ANC y carga rápida USB-C. | Casque circum-aural ANC avec charge rapide USB-C. |
| OG/Twitter title parity | Match | Match | Match |
| hreflang | en-US | es-ES | fr-FR |
| JSON-LD name | Match visible H1 | Match visible H1 | Match visible H1 |

### Before/after snippet
```html
<!-- Before -->
<link rel="canonical" href="https://shop.example.com/products/wireless-headset" />
<meta property="og:title" content="Best headphones" />

<!-- After -->
<link rel="canonical" href="https://shop.example.com/es/productos/auriculares-inalambricos" />
<link rel="alternate" hreflang="en-US" href="https://shop.example.com/en/products/wireless-headset" />
<link rel="alternate" hreflang="es-ES" href="https://shop.example.com/es/productos/auriculares-inalambricos" />
<link rel="alternate" hreflang="fr-FR" href="https://shop.example.com/fr/produits/casque-sans-fil" />
<meta property="og:title" content="Auriculares inalámbricos - batería 30 h" />
```

### Acceptance checks
- Canonical URL matches active locale route.
- OG/Twitter title and description match visible page content.
- JSON-LD product name equals localized H1.
