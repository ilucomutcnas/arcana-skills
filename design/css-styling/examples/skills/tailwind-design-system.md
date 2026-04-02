# Tailwind Design System — Examples

## Semantic Colors

```tsx
// Incorrect — raw colors
<div className="bg-blue-500 text-white">
  <p className="text-gray-600">Secondary</p>
</div>

// Correct — semantic tokens
<div className="bg-primary text-primary-foreground">
  <p className="text-muted-foreground">Secondary</p>
</div>
```

## Built-in Variants First

```tsx
// Incorrect — manual styling
<Button className="border border-input bg-transparent hover:bg-accent">
  Click me
</Button>

// Correct — variant prop
<Button variant="outline">Click me</Button>
```

## className for Layout Only

```tsx
// Incorrect — overriding colors
<Card className="bg-blue-100 text-blue-900 font-bold">

// Correct — layout only
<Card className="max-w-md mx-auto">
```

## Conditional Classes with cn()

```tsx
import { cn } from "@/lib/utils"

// Incorrect
<div className={`flex ${isActive ? "bg-primary" : "bg-muted"}`}>

// Correct
<div className={cn("flex items-center", isActive ? "bg-primary text-primary-foreground" : "bg-muted")}>
```

## Utility Preferences

- `gap-4` not `space-y-4`
- `size-10` not `w-10 h-10`
- `truncate` not `overflow-hidden text-ellipsis whitespace-nowrap`

## Status Indicators

```tsx
// Incorrect — raw colors
<span className="text-emerald-600">+20.1%</span>

// Correct — semantic tokens or Badge
<Badge variant="secondary">+20.1%</Badge>
<span className="text-destructive">-3.2%</span>
```

For detailed implementation patterns, see `tailwind-design-system__resources/implementation-playbook.md`.
