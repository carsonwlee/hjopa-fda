# HJOPA - HondaJet Flight Scoring Envelope

## Overall Weights
### nan

| Evaluate   | Weight   | Tolerance Lower   | Tolerance Upper   | Tolerance Unit   | Evaluate lower limit   | Evaluate upper limit   | Evaluation Unit   |
|------------|----------|-------------------|-------------------|------------------|------------------------|------------------------|-------------------|

## Instrument Approach
### Approaches

| Evaluate                                                     | Weight   |   Tolerance Lower |   Tolerance Upper | Tolerance Unit   |   Evaluate lower limit |   Evaluate upper limit | Evaluation Unit   |
|:-------------------------------------------------------------|:---------|------------------:|------------------:|:-----------------|-----------------------:|-----------------------:|:------------------|
| Altitude at Fixes (GPS)                                      | 4%       |            -100   |             nan   | ft               |                    nan |                    nan | nan               |
| Altitude at Fixes (Baro)                                     | 5%       |            -100   |             nan   | ft               |                    500 |                   1000 | ft AGL            |
| Airspeed within range 1000'-500' Non-Circling [Vref+]        | 2%       |               0   |              15   | kts              |                    500 |                   1000 | ft AGL            |
| Airspeed within range 1000'-500', Circling [Vref+]           | 2%       |              15   |              25   | kts              |                    500 |                   1000 | ft AGL            |
| Airspeed within range 500' AGL to THLD [Vref+]               | 3%       |              -2   |              10   | kts              |                    500 |                   1000 | ft AGL            |
| ILS GS accuracy                                              | 5%       |              -1   |               1   | dots             |                    nan |                    nan | nan               |
| ILS LOC accuracy                                             | 5%       |              -1   |               1   | dots             |                    nan |                    nan | nan               |
| Lateral accuracy after FAF (GPS approach)                    | 5%       |              -1   |               1   | dots             |                    nan |                    nan | nan               |
| VOR course accuracy after FAF                                | 5%       |              -6   |               6   | deg              |                    nan |                    nan | nan               |
| Airspeed consistency                                         | 3%       |             -10   |              10   | kts              |                    nan |                    nan | nan               |
| Vertical speed within range (normal descent)                 | 2%       |           -1000   |            -300   | fpm              |                    nan |                    nan | nan               |
| Vertical speed within range (steep "dive" of dive and drive) | 2%       |           -1100   |            -650   | fpm              |                    nan |                    nan | nan               |
| Vertical speed consistency                                   | 3%       |            -300   |             300   | fpm              |                    nan |                    nan | nan               |
| Circling within the protected area                           | 5%       |               0   |               0.1 | nm               |                    nan |                    nan | nan               |
| Circling speed                                               | 5%       |              15   |              25   | kts              |                    nan |                    nan | nan               |
| TRK over THLD                                                | 3%       |              -1.5 |               1.5 | deg              |                    nan |                    nan | nan               |
| THLD crossing AGL (TCH+)                                     | 6%       |               0   |              30   | ft               |                    nan |                    nan | nan               |
| THLD crossing AGL above min                                  | 6%       |               5   |              10   | ft               |                    nan |                    nan | nan               |
| THLD-crossing IAS [Vref+]                                    | 6%       |              -5   |              10   | kts              |                    nan |                    nan | nan               |
| IAS at TD [Vref+]                                            | 4%       |             -20   |              -6   | kts              |                    nan |                    nan | nan               |
| Touchdown Distance from THLD (1000+)                         | 4%       |            -600   |            1000   | ft               |                    nan |                    nan | nan               |
| Touchdown Distance from centerline                           | 4%       |               0   |              15   | ft               |                    nan |                    nan | nan               |
| Touchdown Norm Acceleration                                  | 3%       |               1   |               1.3 | g                |                    nan |                    nan | nan               |
| Touchdown Lateral Acceleration                               | 5%       |               0   |               0.3 | g                |                    nan |                    nan | nan               |
| Minimum Runway Remaining, relative to SOP/MRR_TD             | 6%       |            -200   |            -200   | ft               |                    nan |                    nan | nan               |

## Safe departure IAS
### Maneuvers

| Evaluate                      | Weight   |   Tolerance Lower |   Tolerance Upper | Tolerance Unit   |   Evaluate lower limit |   Evaluate upper limit | Evaluation Unit   |
|:------------------------------|:---------|------------------:|------------------:|:-----------------|-----------------------:|-----------------------:|:------------------|
| Airspeed above Vx [EFIS data] | 17%      |                -1 |               nan | kts              |                     30 |                    150 | ft AGL            |
| Airspeed above Vy [EFIS data] | 33%      |                -1 |               nan | kts              |                    150 |                   1000 | ft AGL            |

## Stabilized Visual approach
### Approaches

| Evaluate                                         | Weight   |   Tolerance Lower |   Tolerance Upper | Tolerance Unit   |   Evaluate lower limit |   Evaluate upper limit | Evaluation Unit   |
|:-------------------------------------------------|:---------|------------------:|------------------:|:-----------------|-----------------------:|-----------------------:|:------------------|
| Airspeed within range [Vref+]                    | 9%       |                -5 |              10   | kts              |                     50 |                    500 | ft AGL            |
| Airspeed consistency                             | 5%       |               -10 |              10   | kts              |                    nan |                    nan | nan               |
| Vertical speed within range                      | 5%       |              -800 |            -300   | fpm              |                     50 |                    500 | nan               |
| Vertical speed consistency                       | 5%       |              -300 |             300   | fpm              |                     50 |                    500 | nan               |
| Vertical speed consistency                       | 5%       |              -300 |             300   | fpm              |                     50 |                    500 | nan               |
| Centerline Deviation                             | 5%       |                -5 |               5   | deg              |                    nan |                    nan | nan               |
| THLD crossing AGL (TCH+)                         | 12%      |                 0 |              30   | ft               |                    nan |                    nan | nan               |
| THLD crossing AGL above min                      | 2%       |                 5 |              20   | ft               |                    nan |                    nan | nan               |
| THLD-crossing IAS [Vref+]                        | 0%       |                -5 |              10   | kts              |                    nan |                    nan | nan               |
| IAS over 50 AGL [Vref+]                          | 12%      |                -5 |              15   | kts              |                    nan |                    nan | nan               |
| IAS at TD [Vref+]                                | 7%       |               -20 |              -6   | kts              |                    nan |                    nan | nan               |
| Touchdown Distance from THLD (1000+)             | 0%       |              -600 |            1000   | ft               |                    nan |                    nan | nan               |
| Touchdown Distance from 50 AGL                   | 7%       |               700 |            1600   | ft               |                    nan |                    nan | nan               |
| Touchdown Distance from centerline               | 7%       |                 0 |              15   | ft               |                    nan |                    nan | nan               |
| Touchdown Norm Acceleration                      | 5%       |                 1 |               1.3 | g                |                    nan |                    nan | nan               |
| Touchdown Lateral Acceleration                   | 9%       |                 0 |               0.3 | g                |                    nan |                    nan | nan               |
| Minimum Runway Remaining, relative to SOP/MRR_TD | 12%      |              -200 |            -200   | ft               |                    nan |                    nan | nan               |

