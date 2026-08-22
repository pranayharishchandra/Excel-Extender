## 1. We should stop using column numbers.
### redesign the configuration system so it's header-driven instead of column-index-driven.

Why Header-Based Config is Better

Instead of saying

Column A = Sheet Name
Column B = Template Row
Column C = Rows per Material

we say

Find the column whose header is

"Sheet Name"

So if tomorrow your config becomes

Preserve Existing	Managed Columns	Sheet Name	Rows per Material	Template Start Row

Nothing breaks.

The engine finds the headers automatically.
