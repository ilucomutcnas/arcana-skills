# Frontend Dev Guidelines — Examples

## Canonical Component Template

```ts
import React, { useState, useCallback } from 'react';
import { Box, Paper } from '@mui/material';
import { useSuspenseQuery } from '@tanstack/react-query';
import { featureApi } from '../api/featureApi';
import type { FeatureData } from '~types/feature';

interface MyComponentProps {
  id: number;
  onAction?: () => void;
}

export const MyComponent: React.FC<MyComponentProps> = ({ id, onAction }) => {
  const [state, setState] = useState('');

  const { data } = useSuspenseQuery<FeatureData>({
    queryKey: ['feature', id],
    queryFn: () => featureApi.getFeature(id),
  });

  const handleAction = useCallback(() => {
    setState('updated');
    onAction?.();
  }, [onAction]);

  return (
    <Box sx={{ p: 2 }}>
      <Paper sx={{ p: 3 }}>
        {/* Content */}
      </Paper>
    </Box>
  );
};

export default MyComponent;
```

## Canonical File Structure

```
src/
  features/
    my-feature/
      api/
      components/
      hooks/
      helpers/
      types/
      index.ts

  components/
    SuspenseLoader/
    CustomAppBar/

  routes/
    my-route/
      index.tsx
```

## New Component Checklist

- [ ] `React.FC<Props>` with explicit props interface
- [ ] Lazy loaded if non-trivial
- [ ] Wrapped in `<SuspenseLoader>`
- [ ] Uses `useSuspenseQuery` for data
- [ ] No early returns
- [ ] Handlers wrapped in `useCallback`
- [ ] Default export at bottom

## FFCI Score Formula

```
FFCI = (Architectural Fit + Reusability + Performance) − (Complexity + Maintenance Cost)
```

| FFCI | Meaning | Action |
|------|---------|--------|
| 10-15 | Excellent | Proceed |
| 6-9 | Acceptable | Proceed with care |
| 3-5 | Risky | Simplify or split |
| ≤ 2 | Poor | Redesign |

## Anti-Patterns (Immediate Rejection)

- Early loading returns
- Feature logic in `components/`
- Shared state via prop drilling
- Inline API calls
- Untyped responses
- Multiple responsibilities in one component

For deep reference guides, see `frontend-dev-guidelines__resources/`.
