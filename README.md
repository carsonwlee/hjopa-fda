# HJOPA - HondaJet Flight Scoring Envelope

## Instrument Approach
### Approaches

| Evaluate                                                     | Weight   |   Tolerance Lower | Tolerance Upper   | Tolerance Unit   | Evaluate lower limit   | Evaluate upper limit   | Evaluation Unit   |
|:-------------------------------------------------------------|:---------|------------------:|:------------------|:-----------------|:-----------------------|:-----------------------|:------------------|
| Altitude at Fixes (GPS)                                      | 1%       |            -100   | N/A               | ft               | N/A                    | N/A                    | N/A               |
| Altitude at Fixes (Baro)                                     | 1%       |            -100   | N/A               | ft               | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed within range 1000'-500' Non-Circling [Vref+]        | 2%       |              -5   | 20.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed within range 1000'-500', Circling [Vref+]           | 2%       |               5   | 20.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed within range 500' AGL to THLD [Vref+]               | 9%       |              -5   | 5.0               | kts              | 500.0                  | 1000.0                 | ft AGL            |
| ILS GS accuracy                                              | 1%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| ILS LOC accuracy                                             | 1%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| Lateral accuracy after FAF (GPS approach)                    | 1%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| VOR course accuracy after FAF                                | 1%       |              -6   | 6.0               | deg              | N/A                    | N/A                    | N/A               |
| Airspeed consistency                                         | 1%       |             -10   | 10.0              | kts              | N/A                    | N/A                    | N/A               |
| Vertical speed within range (normal descent)                 | 1%       |           -1000   | -300.0            | fpm              | N/A                    | N/A                    | N/A               |
| Vertical speed within range (steep "dive" of dive and drive) | 1%       |           -1100   | -650.0            | fpm              | N/A                    | N/A                    | N/A               |
| Vertical speed consistency                                   | 1%       |            -300   | 300.0             | fpm              | N/A                    | N/A                    | N/A               |
| Circling within the protected area                           | 1%       |               0   | 0.1               | nm               | N/A                    | N/A                    | N/A               |
| Circling speed (relative to VRFF)                            | 5%       |              15   | 25.0              | kts              | N/A                    | N/A                    | N/A               |
| TRK over THLD                                                | 3%       |              -1.5 | 1.5               | deg              | N/A                    | N/A                    | N/A               |
| THLD crossing AGL (TCH+)                                     | 15%      |               0   | 30.0              | ft               | N/A                    | N/A                    | N/A               |
| THLD crossing AGL above min                                  | 5%       |               5   | 10.0              | ft               | N/A                    | N/A                    | N/A               |
| THLD-crossing IAS [Vref+]                                    | 19%      |              -5   | 3.0               | kts              | N/A                    | N/A                    | N/A               |
| IAS at TD [Vref+]                                            | 24%      |             -10   | 0.0               | kts              | N/A                    | N/A                    | N/A               |
| Touchdown Distance from THLD (1000+)                         | 8%       |            -200   | 200.0             | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Distance from centerline                           | 5%       |               0   | 15.0              | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Norm Acceleration                                  | 5%       |               1.3 | 1.5               | g                | N/A                    | N/A                    | N/A               |
| Touchdown Lateral Acceleration                               | 3%       |               0   | 0.3               | g                | N/A                    | N/A                    | N/A               |
| Minimum Runway Remaining, relative to SOP/MRR_TD             | 7%       |               0   | 0.0               | ft               | N/A                    | N/A                    | N/A               |

## Stabilized Visual approach
### Approaches

| Evaluate                                         | Weight   |   Tolerance Lower |   Tolerance Upper | Tolerance Unit   | Evaluate lower limit   | Evaluate upper limit   | Evaluation Unit   |
|:-------------------------------------------------|:---------|------------------:|------------------:|:-----------------|:-----------------------|:-----------------------|:------------------|
| Airspeed within range [Vref+]                    | 5%       |              -5   |              10   | kts              | 50.0                   | 500.0                  | ft AGL            |
| Airspeed consistency                             | 5%       |             -10   |              10   | kts              | N/A                    | N/A                    | N/A               |
| Vertical speed within range                      | 2%       |            -800   |            -300   | fpm              | 50.0                   | 500.0                  | N/A               |
| Vertical speed consistency                       | 2%       |            -300   |             300   | fpm              | 50.0                   | 500.0                  | N/A               |
| Centerline Deviation                             | 5%       |              -5   |               5   | deg              | N/A                    | N/A                    | N/A               |
| THLD crossing AGL (TCH+)                         | 15%      |               0   |              30   | ft               | N/A                    | N/A                    | N/A               |
| THLD crossing AGL above min                      | 3%       |               5   |              20   | ft               | N/A                    | N/A                    | N/A               |
| THLD-crossing IAS [Vref+]                        | 10%      |              -2   |               2   | kts              | N/A                    | N/A                    | N/A               |
| IAS over 50 AGL [Vref+]                          | 25%      |              -5   |               5   | kts              | N/A                    | N/A                    | N/A               |
| IAS at TD [Vref+]                                | 25%      |             -10   |               0   | kts              | N/A                    | N/A                    | N/A               |
| Touchdown Distance from THLD (1000+)             | 8%       |            -200   |             200   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Distance from 50 AGL                   | 8%       |             800   |            1200   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Distance from centerline               | 5%       |               0   |              15   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown Norm Acceleration                      | 5%       |               1.3 |               1.5 | g                | N/A                    | N/A                    | N/A               |
| Touchdown Lateral Acceleration                   | 3%       |               0   |               0.3 | g                | N/A                    | N/A                    | N/A               |
| Minimum Runway Remaining, relative to SOP/MRR_TD | 11%      |               0   |               0   | ft               | N/A                    | N/A                    | N/A               |

## Standard Operating Parameters

| Characteristic          |   Value |
|:------------------------|--------:|
| Min runway at touchdown |    2100 |

## Flight Data Analysis

| All   | VFR   | IFR   | Evaluate                     |   Caution Lower |   Caution Upper | Unit   |
|:------|:------|:------|:-----------------------------|----------------:|----------------:|:-------|
| x     |       |       | Max bank in flight           |              60 |              70 | bank   |
| x     |       |       | Max speed below 10000ft      |             260 |             270 | IAS    |
| x     |       |       | Max taxi speed               |              30 |              35 | gs     |
| x     |       |       | Pitch - high below 1000ft    |              17 |              19 | pitch  |
| x     |       |       | Pitch - high below 200ft     |              17 |              19 | pitch  |
| x     |       |       | Pitch - high below 200ft     |              17 |              19 | pitch  |
| x     |       |       | Pitch - low below 1000ft     |             -11 |             -13 | pitch  |
| x     |       |       | Pitch - low below 200ft      |             -11 |             -13 | pitch  |
| x     |       |       | Pitch - low below 50ft       |              -9 |             -11 | pitch  |
| x     |       |       | Pitch - low below 20ft       |              -3 |              -4 | pitch  |
| x     |       |       | Bank - max below 1000ft      |              45 |              50 | bank   |
| x     |       |       | Bank - max below 200ft       |              30 |              40 | bank   |
| x     |       |       | Sink rate - max below 1000ft |           -2000 |           -2500 | VS     |
| x     |       |       | Sink rate - max below 500ft  |           -1300 |           -1500 | VS     |
| x     |       |       | Sink rate - max below 200ft  |           -1300 |           -1500 | VS     |
| x     |       |       | N1 - max below 500ft         |              60 |              65 | N1     |
| x     |       |       | N1 - min below 200ft         |              40 |              45 | N1     |
| x     |       |       | Outside extnd. RW below 200  |               1 |              10 | ft     |
| x     |       |       | IAS - max below 1000         |             120 |             140 | ft     |
| x     |       |       | IAS - max below 500          |             120 |             140 | ft     |
| x     |       |       | IAS - max below 200          |             120 |             140 | ft     |
| x     |       |       | AP - engage altitude AFE     |             499 |             500 | ft     |
| x     |       |       | AP - disengage altitude AFE  |             100 |             101 | ft     |
| x     |       |       | IAS-Vref - high below 200    |              10 |              15 | kts    |
| x     |       |       | IAS-Vref - low below 200     |              -6 |             -10 | kts    |
| x     |       |       | IAS-Vref - high at 50' AGL   |               5 |              10 | kts    |
| x     |       |       | IAS-Vref - low at 50' AGL    |              -6 |             -10 | kts    |
|       |       | x     | Configured fully - AFE       |             900 |             700 | ft     |
|       | x     |       | Configured fully - AFE       |             900 |             700 | ft     |
| x     |       |       | THLD - high IAS-Vref         |               5 |              10 | ft     |
| x     |       |       | THLD - low IAS-Vref          |              -6 |             -10 | ft     |
| x     |       |       | THLD - high AGL-TCH          |              30 |              50 | ft     |
| x     |       |       | THLD - low AGL-TCH           |             -14 |             -19 | ft     |
| x     |       |       | THLD - low AGL               |              10 |              20 | ft     |
| x     |       |       | Touchdown distance - long    |            1500 |            2000 | ft     |
| x     |       |       | Touchdown distance - short   |             200 |             100 | ft     |
| x     |       |       | RWY remaining @40 kts        |             600 |             400 | ft     |
| x     |       |       | RWY remaining @70 kts        |            1300 |            1000 | ft     |

