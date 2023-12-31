# HJOPA - HondaJet Flight Scoring Envelope

## Overall Weights

| Evaluate   | Weight   |
|:-----------|:---------|
| Maneuvers  | 25%      |
| Approaches | 75%      |

## Instrument Approach
### Approaches

| Evaluate                                                     | Weight   |   Tolerance Lower | Tolerance Upper   | Tolerance Unit   | Evaluate lower limit   | Evaluate upper limit   | Evaluation Unit   |
|:-------------------------------------------------------------|:---------|------------------:|:------------------|:-----------------|:-----------------------|:-----------------------|:------------------|
| Altitude at Fixes (GPS)                                      | 4%       |            -100   | N/A               | ft               | N/A                    | N/A                    | N/A               |
| Altitude at Fixes (Baro)                                     | 5%       |            -100   | N/A               | ft               | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed within range 1000'-500' Non-Circling [Vref+]        | 2%       |               0   | 15.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed within range 1000'-500', Circling [Vref+]           | 2%       |              15   | 25.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed within range 500' AGL to THLD [Vref+]               | 3%       |              -2   | 10.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| ILS GS accuracy                                              | 5%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| ILS LOC accuracy                                             | 5%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| Lateral accuracy after FAF (GPS approach)                    | 5%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| VOR course accuracy after FAF                                | 5%       |              -6   | 6.0               | deg              | N/A                    | N/A                    | N/A               |
| Airspeed consistency                                         | 3%       |             -10   | 10.0              | kts              | N/A                    | N/A                    | N/A               |
| Vertical speed within range (normal descent)                 | 2%       |           -1000   | -300.0            | fpm              | N/A                    | N/A                    | N/A               |
| Vertical speed within range (steep "dive" of dive and drive) | 2%       |           -1100   | -650.0            | fpm              | N/A                    | N/A                    | N/A               |
| Vertical speed consistency                                   | 3%       |            -300   | 300.0             | fpm              | N/A                    | N/A                    | N/A               |
| Circling within the protected area                           | 5%       |               0   | 0.1               | nm               | N/A                    | N/A                    | N/A               |
| Circling speed                                               | 5%       |              15   | 25.0              | kts              | N/A                    | N/A                    | N/A               |
| TRK over THLD                                                | 3%       |              -1.5 | 1.5               | deg              | N/A                    | N/A                    | N/A               |
| THLD crossing AGL (TCH+)                                     | 6%       |               0   | 30.0              | ft               | N/A                    | N/A                    | N/A               |
| THLD crossing AGL above min                                  | 6%       |               5   | 10.0              | ft               | N/A                    | N/A                    | N/A               |
| THLD-crossing IAS [Vref+]                                    | 6%       |              -5   | 10.0              | kts              | N/A                    | N/A                    | N/A               |
| IAS at TD [Vref+]                                            | 4%       |             -20   | -6.0              | kts              | N/A                    | N/A                    | N/A               |
| Touchdown Distance from THLD (1000+)                         | 4%       |            -600   | 1000.0            | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Distance from centerline                           | 4%       |               0   | 15.0              | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Norm Acceleration                                  | 3%       |               1   | 1.3               | g                | N/A                    | N/A                    | N/A               |
| Touchdown Lateral Acceleration                               | 5%       |               0   | 0.3               | g                | N/A                    | N/A                    | N/A               |
| Minimum Runway Remaining, relative to SOP/MRR_TD             | 6%       |            -200   | -200.0            | ft               | N/A                    | N/A                    | N/A               |

## Safe departure IAS
### Maneuvers

| Evaluate                      | Weight   |   Tolerance Lower | Tolerance Upper   | Tolerance Unit   |   Evaluate lower limit |   Evaluate upper limit | Evaluation Unit   |
|:------------------------------|:---------|------------------:|:------------------|:-----------------|-----------------------:|-----------------------:|:------------------|
| Airspeed above Vx [EFIS data] | 17%      |                -1 | N/A               | kts              |                     30 |                    150 | ft AGL            |
| Airspeed above Vy [EFIS data] | 33%      |                -1 | N/A               | kts              |                    150 |                   1000 | ft AGL            |

## Stabilized Visual approach
### Approaches

| Evaluate                                         | Weight   |   Tolerance Lower |   Tolerance Upper | Tolerance Unit   | Evaluate lower limit   | Evaluate upper limit   | Evaluation Unit   |
|:-------------------------------------------------|:---------|------------------:|------------------:|:-----------------|:-----------------------|:-----------------------|:------------------|
| Airspeed within range [Vref+]                    | 9%       |                -5 |              10   | kts              | 50.0                   | 500.0                  | ft AGL            |
| Airspeed consistency                             | 5%       |               -10 |              10   | kts              | N/A                    | N/A                    | N/A               |
| Vertical speed within range                      | 5%       |              -800 |            -300   | fpm              | 50.0                   | 500.0                  | N/A               |
| Vertical speed consistency                       | 5%       |              -300 |             300   | fpm              | 50.0                   | 500.0                  | N/A               |
| Vertical speed consistency                       | 5%       |              -300 |             300   | fpm              | 50.0                   | 500.0                  | N/A               |
| Centerline Deviation                             | 5%       |                -5 |               5   | deg              | N/A                    | N/A                    | N/A               |
| THLD crossing AGL (TCH+)                         | 12%      |                 0 |              30   | ft               | N/A                    | N/A                    | N/A               |
| THLD crossing AGL above min                      | 2%       |                 5 |              20   | ft               | N/A                    | N/A                    | N/A               |
| THLD-crossing IAS [Vref+]                        | 0%       |                -5 |              10   | kts              | N/A                    | N/A                    | N/A               |
| IAS over 50 AGL [Vref+]                          | 12%      |                -5 |              15   | kts              | N/A                    | N/A                    | N/A               |
| IAS at TD [Vref+]                                | 7%       |               -20 |              -6   | kts              | N/A                    | N/A                    | N/A               |
| Touchdown Distance from THLD (1000+)             | 0%       |              -600 |            1000   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Distance from 50 AGL                   | 7%       |               700 |            1600   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Distance from centerline               | 7%       |                 0 |              15   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Norm Acceleration                      | 5%       |                 1 |               1.3 | g                | N/A                    | N/A                    | N/A               |
| Touchdown Lateral Acceleration                   | 9%       |                 0 |               0.3 | g                | N/A                    | N/A                    | N/A               |
| Minimum Runway Remaining, relative to SOP/MRR_TD | 12%      |              -200 |            -200   | ft               | N/A                    | N/A                    | N/A               |

