# HJOPA - HondaJet Flight Scoring Envelope

## Weighting Rationale: Physics-First Approach to Runway Excursion Prevention

The scoring weights in this system are not arbitrary—they reflect a **physics-first approach** grounded in three key pillars: historical HondaJet accident data, fundamental physical relationships, and aircraft-specific design limitations. This ensures the scoring system prioritizes factors that directly contribute to preventing runway excursions.

### Why This Approach Matters

Runway excursions represent the most significant landing risk for the HondaJet. Our weighting system addresses this by heavily emphasizing the factors that have been statistically linked to the majority of HondaJet runway excursions, while accounting for the physical relationships that make speed errors exponentially dangerous.

### Key Principles

1. **Historical Data Priority**: Factors linked to actual HondaJet runway excursions receive higher weights
2. **Physical Relationships**: Factors with quadratic relationships (speed² effects) are weighted more heavily due to their exponential impact
3. **Aircraft-Specific Design**: HondaJet limitations (no thrust reversers, limited ground spoilers) amplify the importance of energy management
4. **Direct vs. Indirect Impact**: Measurements at critical points (threshold/touchdown) are weighted higher than predictive stability metrics

### Why Airspeed Gets the Highest Weights (16-18% at threshold, 14-16% at touchdown)

**Historical Evidence**: Excessive airspeed has been identified as a primary factor in nearly all HondaJet runway excursions. Pilots often add unnecessary speed to VREF calculations, which becomes increasingly problematic closer to touchdown.

**Physics: The Exponential Penalty**

Speed errors create a compounding problem due to quadratic relationships:

- **Kinetic Energy**: Doubles with only a ~41% speed increase (KE = ½mv²)
  - Example: +10 kt over VREF (at ~108 kt) = ~19% more energy to dissipate
  - The brakes must absorb this additional energy, requiring more runway

- **Lift**: Also grows quadratically with speed (L = ½ρV²SCL)
  - More lift = less weight on wheels = less braking force available
  - Touchdown at higher speeds occurs at lower angle of attack, reducing ability to dump lift by lowering the nose
  - This prolongs ground roll and reduces stopping effectiveness

- **The Double Penalty**: Excess speed means you have:
  1. More energy to dissipate (kinetic energy)
  2. Less ability to dissipate it (reduced braking force from residual lift)

**Aircraft-Specific Amplification**: Without thrust reversers and with limited ground spoilers (Elite II only, partial coverage), the HondaJet relies heavily on brake effectiveness. Excess speed directly compromises this critical deceleration method.

### Why Touchdown Position and Runway Remaining Matter (12-14%)

Second only to airspeed, these factors directly determine whether sufficient runway remains to stop safely:

- **Touchdown Distance from Threshold (12-13%)**: Early touchdown maximizes available runway length for deceleration. Late touchdown, especially when combined with excess speed, severely limits safety margins.

- **Runway Remaining at Touchdown (13-14%)**: This is a direct outcome measurement—how much runway is left when the aircraft touches down. With brake-limited deceleration, every foot counts.

These factors interact: being high or fast over the threshold directly affects touchdown position, which on shorter runways can be decisive in avoiding an excursion.

### Why Stability Metrics Are Weighted Lower (2-3%)

Stability metrics like "Airspeed consistent" and "Vertical speed consistent" receive lower weights (typically 2%) not because they're unimportant, but because they serve a **predictive/supporting role** rather than being direct measurements of excursion risk.

- They provide early warning of potential problems
- Statistical correlation shows that unstable approaches lead to poorer threshold performance
- However, the physics of excursion risk hinge on conditions **at the threshold and touchdown**, not earlier in the approach
- These metrics support the primary factors by helping ensure pilots reach the threshold in a controlled state

### Why Navigation/Procedural Items Are Weighted Minimally (1-2%)

Items like ILS glideslope deviation, localizer deviation, and crossing altitudes receive minimal weights (1-2%) because:

- They are important for procedural compliance and training
- However, they have not been statistically prominent as primary causes in HondaJet excursion data
- They contribute indirectly to safety but don't directly measure the energy management factors that drive excursion risk
- Every item still receives at least minimal weight to ensure comprehensive coverage

### Weight Distribution Summary

**Instrument Approaches**:
- **Airspeed metrics**: 42% total (cumulative across approach phases, with highest at threshold/touchdown)
- **Touchdown/runway factors**: 25% (touchdown distance + runway remaining)
- **Critical factors combined**: 67% of total weight on the highest-risk elements

**Visual Approaches**:
- **Airspeed metrics**: 50% total (even higher emphasis due to lack of glideslope guidance)
- **Touchdown/runway factors**: 27% 
- **Critical factors combined**: 77% of total weight

All weight categories total 100%, ensuring complete scoring coverage while prioritizing factors with the greatest impact on runway safety.

### Operational Implications

This weighting structure guides pilots toward:
- **Tight speed control** at threshold and touchdown (no speed additions to VREF)
- **Early touchdown** to maximize runway for brake-limited stopping
- **Go-around decisions** if conditions at 50' AGL or threshold are not ideal
- **Awareness** that small speed errors create exponential energy increases

The weights aren't just numbers—they reflect real physics, real aircraft limitations, and real historical outcomes. When the system emphasizes airspeed control heavily, it's because physics and accident data tell us that's where the biggest risk lies.

---

*This weighting rationale is based on historical HondaJet excursion data, fundamental aerodynamic and kinetic energy relationships, and the aircraft's specific design constraints. For technical details on the weighting methodology, see `LLM_Scoring_Guidance.md`.*

---

## Instrument Approach
### Approaches

| Evaluate                                                   | Weight   |   Tolerance Lower | Tolerance Upper   | Tolerance Unit   | Evaluate lower limit   | Evaluate upper limit   | Evaluation Unit   |
|:-----------------------------------------------------------|:---------|------------------:|:------------------|:-----------------|:-----------------------|:-----------------------|:------------------|
| Crossing altitudes maintained (GPS)                        | 1%       |            -100   | N/A               | ft               | N/A                    | N/A                    | N/A               |
| Crossing altitudes maintained (Baro)                       | 1%       |            -100   | N/A               | ft               | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed from 1000' AFE to 500' AFE (non-circling) [Vref+] | 3%       |              -5   | 20.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed from 1000' AFE to 500' AFE (circling) [Vref+]     | 2%       |               5   | 20.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| Airspeed from 500' AFE to threshold [Vref+]                | 12%      |              -5   | 10.0              | kts              | 500.0                  | 1000.0                 | ft AGL            |
| ILS glideslope deviation (2 dots=fsd)                      | 2%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| ILS localizer deviation (2 dots=fsd)                       | 1%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| Deviation from GPS course after FAF (2 dots=fsd)           | 1%       |              -1   | 1.0               | dots             | N/A                    | N/A                    | N/A               |
| Deviation from VOR course after FAF                        | 1%       |              -6   | 6.0               | deg              | N/A                    | N/A                    | N/A               |
| Airspeed consistent                                        | 2%       |             -10   | 10.0              | kts              | N/A                    | N/A                    | N/A               |
| Sink rate range in IAP                                     | 1%       |           -1000   | -300.0            | fpm              | N/A                    | N/A                    | N/A               |
| Sink rate range in IAP "dive"                              | 1%       |           -1100   | -650.0            | fpm              | N/A                    | N/A                    | N/A               |
| Vertical speed consistent                                  | 2%       |            -300   | 300.0             | fpm              | N/A                    | N/A                    | N/A               |
| Circling within the protected area                         | 1%       |               0   | 0.1               | nm               | N/A                    | N/A                    | N/A               |
| Circling speed (relative to VRFF)                          | 1%       |              15   | 25.0              | kts              | N/A                    | N/A                    | N/A               |
| Track over threshold aligned with runway                   | 3%       |              -1.5 | 1.5               | deg              | N/A                    | N/A                    | N/A               |
| Altitude AGL at threshold (TCH+)                           | 4%       |               0   | 30.0              | ft               | N/A                    | N/A                    | N/A               |
| Altitude AGL at threshold above min                        | 3%       |               5   | 10.0              | ft               | N/A                    | N/A                    | N/A               |
| Airspeed over threshold [Vref+]                            | 16%      |              -5   | 3.0               | kts              | N/A                    | N/A                    | N/A               |
| Airspeed at touchdown [Vref+]                              | 14%      |             -10   | 0.0               | kts              | N/A                    | N/A                    | N/A               |
| Touchdown distance from threshold                          | 12%      |            -200   | 200.0             | ft               | N/A                    | N/A                    | N/A               |
| Touchdown distance from centerline                         | 1%       |               0   | 15.0              | ft               | N/A                    | N/A                    | N/A               |
| Vertical acceleration at touchdown                         | 1%       |               1.3 | 1.5               | g                | N/A                    | N/A                    | N/A               |
| Side loading at touchdown                                  | 1%       |               0   | 0.3               | g                | N/A                    | N/A                    | N/A               |
| Runway remaining at touchdown                              | 13%      |               0   | 0.0               | ft               | N/A                    | N/A                    | N/A               |

## Stabilized Visual approach
### Approaches

| Evaluate                                | Weight   |   Tolerance Lower |   Tolerance Upper | Tolerance Unit   | Evaluate lower limit   | Evaluate upper limit   | Evaluation Unit   |
|:----------------------------------------|:---------|------------------:|------------------:|:-----------------|:-----------------------|:-----------------------|:------------------|
| Airspeed within range [Vref+]           | 9%       |              -5   |              10   | kts              | 50.0                   | 500.0                  | ft AGL            |
| Airspeed consistent                     | 2%       |             -10   |              10   | kts              | N/A                    | N/A                    | N/A               |
| Sink rate within range                  | 1%       |            -800   |            -300   | fpm              | 50.0                   | 500.0                  | N/A               |
| Vertical speed consistent               | 2%       |            -300   |             300   | fpm              | 50.0                   | 500.0                  | N/A               |
| Centerline deviation on Final           | 3%       |              -5   |               5   | deg              | N/A                    | N/A                    | N/A               |
| Altitude AGL over threshold (TCH+)      | 5%       |               0   |              30   | ft               | N/A                    | N/A                    | N/A               |
| Altitude AGL over threshold (above min) | 4%       |               5   |              20   | ft               | N/A                    | N/A                    | N/A               |
| Airspeed over threshold [Vref+]         | 18%      |              -2   |               2   | kts              | N/A                    | N/A                    | N/A               |
| Airspeed at 50 AGL [Vref+]              | 7%       |              -5   |               5   | kts              | N/A                    | N/A                    | N/A               |
| Airspeed at touchdown [Vref+]           | 16%      |             -10   |               0   | kts              | N/A                    | N/A                    | N/A               |
| Touchdown distance from threshold       | 13%      |            -200   |             200   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown distance from 50 AGL          | 3%       |             800   |            1200   | ft               | N/A                    | N/A                    | N/A               |
| Touchdown distance from centerline      | 1%       |               0   |              15   | ft               | N/A                    | N/A                    | N/A               |
| Vertical acceleration at touchdown      | 1%       |               1.3 |               1.5 | g                | N/A                    | N/A                    | N/A               |
| Side loading at touchdown               | 1%       |               0   |               0.3 | g                | N/A                    | N/A                    | N/A               |
| Runway remaining at touchdown           | 14%      |               0   |               0   | ft               | N/A                    | N/A                    | N/A               |

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

