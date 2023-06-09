# two_strike_proficiency_index

The proposed baseball statistic, Two-Strike Proficiency Index (TSPI), aims to evaluate a batter's effectiveness during two-strike counts. It's a scaled value ranging from 0 to 1, where 1 implies perfect performance with a two-strike count (never striking out, always getting on base or hitting), and 0 indicates a worst-case performance (always striking out, never getting a hit or on base).

TSPI is calculated based on five equally weighted metrics:

1. Two-Strike Strikeout Percentage (TSSO%)
2. Two-Strike Walk Percentage (TSBB%)
3. Two-Strike Batting Average (TSAVG)
4. Two-Strike On-base Plus Slugging (TSOPS)
5. Two-Strike HR Percentage (TSHR%)

The formula for TSPI is as follows:

TSPI = (0.2 * (1 - TSSO%)) + (0.2 * TSBB%) + (0.2 * TSAVG) + (0.2 * TSOPS) + (0.2 * TSHR%)
