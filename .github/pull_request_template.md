<!--
Pull requests are squash-merged, so write the title in the Conventional Commits
style: `fix: ...`, `feat: ...`, `docs: ...`, `refactor: ...`, `test: ...`, `chore: ...`.

CI runs the linters. To catch failures before you push, run:

uvx prek run --all-files
-->

## Summary

<!-- What does this change, and why? -->

## Related issues

<!-- `Closes #123` closes the issue on merge. Remove this section if there are none. -->

## Testing

<!-- How did you check that this works? -->

## Checklist

- [ ] Field descriptions state the unit or format where it is not obvious from the name.
- [ ] [pywttr](https://github.com/monosans/pywttr) and [aiopywttr](https://github.com/monosans/aiopywttr) keep working with this change: their tests check the models against live wttr.in responses.
