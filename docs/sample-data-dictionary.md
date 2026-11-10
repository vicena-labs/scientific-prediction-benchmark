# Vicena scientific data dictionary

> [Vicena](https://vicena.ai/experimental-data) · [Benchmark](../README.md) · [Discuss your data needs](mailto:mehdi@vicena.ai)

Vicena works with scientists to build datasets around real experiments. Explore the measurements, images, process records and expert analysis that can support your AI training and evaluation projects.

Start with the scientific task you want your model to perform. We work with partner laboratories to retrieve historical records, add expert annotation and commission targeted measurements or new experiments around that task.

## Explore the data

| Collection | Scientific scope | Data and formats |
| --- | --- | --- |
| [C01 · Battery measurements](#c01--battery-measurements) | Formulation, preparation and electrochemical performance | XLSX measurement and analysis tables |
| [C02 · Catalyst characterization](#c02--catalyst-characterization) | Structure, morphology, composition and electrochemical response | TXT, JPEG, DOCX and XLSX |
| [C03 · Oxygen electrodes](#c03--oxygen-electrodes) | Electrode characterization, performance and durability | Laboratory dataset specification |
| [C04 · Thin films and 2D materials](#c04--thin-films-and-2d-materials) | Pattern quality, surface topography and film morphology | Microscopy figures and profiles in PPTX |
| [C05 · Coin-cell process recording](#c05--coin-cell-process-recording) | Laboratory actions, equipment and assembly sequence | MP4 with supporting XLSX and PDF records |
| [C06 · Cell biology and immune assays](#c06--cell-biology-and-immune-assays) | Cellular signals, protein expression and assay responses | FCS, TIFF, XLSX and Prism projects |
| [C07 · Immunotherapy results](#c07--immunotherapy-results) | Study groups and animal-level results | XLSX result tables and study figures |
| [C08 · Enzyme kinetics](#c08--enzyme-kinetics) | Variant and substrate comparisons | Reported kinetic parameters and assay context |
| [C09 · Cytometry acquisition records](#c09--cytometry-acquisition-records) | Event-level scatter and fluorescence signals | Native FCS 3.1 files |

## C01 · Battery measurements

**Scientific systems:** electrolyte and additive comparisons across NCM622/graphite, LFP/graphite, nickel-rich and silicon-containing electrode systems, including pouch-cell preparation and testing. **Format:** XLSX.

| Data type | Representation / unit | Scientific content |
| --- | --- | --- |
| Formulations | Material labels and nominal ingredient quantities | Electrolyte recipes, additive comparisons and batch quantities |
| Electrolyte properties | Numerical property tables | Conductivity, moisture and acidity entries |
| Cell preparation | Cell/stage labels; mass in g | Filling, sealing, formation, ageing and grading records |
| Electrical checkpoints | V and mΩ where labelled | Voltage and impedance at preparation and test checkpoints |
| Formation and grading | Capacity in mAh | Charge/discharge and grading-capacity measurements |
| Cycling performance | Cycle index, mAh and calculated % | Capacity trajectories, retention and efficiency summaries |
| Test conditions | °C, V and C-rate where documented | Temperature, voltage limits and planned or recorded charge/discharge settings |
| Rate and resistance | C-rate, mAh, mΩ and state of charge | Capacity across test rates and direct-current resistance measurements |
| Electrochemical curves | Potential-current, dQ/dV and impedance arrays | Voltammetry, differential capacity and impedance response |
| Researcher analysis | Calculations and scientific notes | Performance comparisons, observations and proposed next experiments |

**Project applications:** early-cycle performance prediction, formulation comparison and analysis of preparation and test conditions.

## C02 · Catalyst characterization

**Scientific systems:** Fe-N-C catalyst materials and electrode test configurations. **Formats:** TXT diffraction traces, JPEG microscopy, DOCX elemental reports and XLSX electrochemical records.

| Data type | Representation / unit | Scientific content |
| --- | --- | --- |
| Material and test context | Sample, electrode and test labels | Catalyst identity and measurement configuration |
| X-ray diffraction | Scan-coordinate and intensity arrays | Diffraction response for structural characterization |
| Electron microscopy | SEM images with scale bars and magnification | Surface morphology and microstructural features |
| Elemental spectra and maps | EDS report images | Elemental signals and spatial distribution |
| Elemental quantification | Element/line labels, wt% and report-specific statistics | Composition estimates, reported uncertainty and standard information |
| Electrochemical response | Potential in V; signed current in A | Linear sweeps and multi-cycle cyclic voltammetry |
| Reaction and electrode context | Test labels; RPM where supplied | Oxygen-evolution/reduction measurements and electrode/rotation context |
| Measurement sequence | Ordered scan observations | The progression of response through each recorded sweep |

**Project applications:** electrochemical curve prediction, microscopy interpretation and combined analysis of structure, composition and performance. A companion laboratory specification describes additional metal-N-C catalyst families.

## C03 · Oxygen electrodes

**Scientific systems:** GDC/PBSCF core-shell nanofiber composites and a PBSCF control in symmetric-cell and single-cell configurations. **Record:** laboratory dataset specification covering the following measurement types.

| Data type | Representation | Scientific content |
| --- | --- | --- |
| Material and cell context | Composition and configuration labels | Composite/control identities and cell architecture |
| Diffraction and microscopy | XRD, SEM and selected TEM | Structure and electrode morphology |
| Elemental analysis | EDS spectra/maps | Element distribution in selected materials |
| Surface chemistry | Before/after XPS spectra | Surface-chemical changes associated with testing |
| Impedance | Electrochemical impedance spectroscopy | Response across temperature and operating conditions |
| Polarization | Linear-sweep voltammetry | Fuel-cell and electrolysis-mode response |
| Durability | Current-versus-time records | Sustained response during constant-potential testing |

**Project applications:** scope datasets for electrode comparison, operating-condition analysis and durability prediction.

## C04 · Thin films and 2D materials

**Scientific systems:** lithographed patterns, transferred graphene and multilayer films. **Format:** PPTX containing microscopy figures, AFM views, height profiles and researcher descriptions.

| Data type | Representation | Scientific content |
| --- | --- | --- |
| Pattern microscopy | Image figures with displayed scale information | Pattern edges, linewidth variation and visible defects |
| Surface topography | Atomic force microscopy figures | Surface features in graphene-transfer examples |
| Height profiles | Plotted distance-height relationships | Surface-profile evidence alongside AFM views |
| Film morphology | Image figures | Wrinkles, breaks and other visible film features |
| Researcher descriptions | Scientific text | Fabrication context and expert descriptions of the observed features |

**Project applications:** visual defect recognition, surface-profile interpretation and expert assessment of fabrication quality.

## C05 · Coin-cell process recording

**Scientific workflow:** electrode preparation, coating, coin-cell assembly, equipment handling and test-loading context. **Formats:** MP4, XLSX moment records and PDF supporting material.

| Data type | Representation | Scientific content |
| --- | --- | --- |
| Laboratory video | Time-ordered frames | Visible actions, materials, components and equipment |
| Time references | Video timestamps | Locations of actions and observations within the recording |
| Process stages | Sequence and stage descriptions | Preparation, coating, assembly and testing context |
| Moment annotations | Timestamped text | Descriptions of actions, objects and tool use |
| Laboratory context | Supporting documents | Scientist explanations and workflow clarifications |
| Demonstration annotations | Separate presentation layer | AI-assisted tags and overlays in edited demonstrations |

**Project applications:** process-step recognition, tool and component identification, and scientific workflow understanding. Video and annotation can be scoped as optional capture layers in a new data project.

## C06 · Cell biology and immune assays

**Scientific systems:** glioma-related cell preparations and cellular/immune-response comparisons, including astrocyte, microglial, macrophage and T-cell contexts. **Formats:** FCS, TIFF, XLSX and GraphPad Prism projects.

| Data type | Representation / unit | Scientific content |
| --- | --- | --- |
| Cytometry signals | Event-by-channel numerical arrays | Scatter and fluorescence pulse measurements |
| Acquisition context | Channel definitions and timestamps | Instrument, timing and parameter metadata |
| Protein images | TIFF image exports | Chemiluminescent, colorimetric and composite views |
| Protein quantification | Signal values and calculated ratios | Band-intensity summaries and normalized responses |
| Gene expression | Cycle-threshold values and calculated ratios | Target/reference readings, ΔCt, ΔΔCt and relative expression |
| Viability and cell damage | CCK-8 tables; LDH optical density and U/mL where labelled | Cellular-response measurements and assay calculations |
| Immunoassay calibration | Optical density and standard concentrations | Calibration and sample-response tables |
| Protein/cytokine response | pg/mL or ng/mL as labelled | MIF, LGALS1 and IFNG results |
| Immune-response summaries | Numerical tables and condition labels | Marker, proliferation and T-cell response summaries |
| Researcher analysis | Prism projects and figures | Statistical analysis and scientific presentation |

**Project applications:** assay interpretation, quantitative response analysis and expert annotation of cellular evidence.

## C07 · Immunotherapy results

**Scientific records:** animal-level observations and treatment-group result tables. **Formats:** XLSX, study figures and supporting scientific context.

| Data type | Representation | Scientific content |
| --- | --- | --- |
| Observation identity | Animal identifiers | Row-level indexing within study tables |
| Study groups | Treatment labels | Recorded experimental group assignments |
| Numerical observations | Result tables | Animal-level numerical entries |
| Researcher summaries | Values and calculations | Study result summaries and calculated entries |
| Scientific context | Figures and study descriptions | Researcher presentation of the experimental work |

**Project applications:** expert annotation of study context and analysis of treatment-group result tables.

## C08 · Enzyme kinetics

**Scientific systems:** an L-aspartate β-decarboxylase, wild-type and double-mutant forms, and substrate comparisons. **Record:** DOCX with reported kinetic parameters and assay context.

| Data type | Representation / unit | Scientific content |
| --- | --- | --- |
| Enzyme variant | Categorical labels | Wild-type and mutant identities |
| Substrate | Categorical labels | Substrate associated with each kinetic result |
| `Km` | mM with reported ± term | Michaelis constant |
| `kcat` | s⁻¹ with reported ± term | Turnover parameter |
| `kcat/Km` | mM⁻¹·s⁻¹ | Catalytic efficiency |
| Detection status | Recorded status labels | Detectable and not-detectable responses |
| Assay context | Method and analysis descriptions | HPLC-based product detection and kinetic-analysis context |

**Project applications:** variant/substrate comparisons, kinetic-parameter interpretation and expert-labelled enzyme-performance tasks.

## C09 · Cytometry acquisition records

**Acquisition system:** Attune NxT flow cytometry. **Format:** native FCS 3.1 files with event arrays and acquisition metadata.

| Data type | Representation | Scientific content |
| --- | --- | --- |
| Event identity | Numeric event field | Ordering within an acquisition |
| Acquisition time | Header-defined timing scale | Timing coordinate for recorded events |
| Scatter signals | Floating-point pulse measurements | Forward/side scatter area, height and width |
| Fluorescence signals | Floating-point pulse measurements | BL/YL channel area, height and width measurements |
| Parameter definitions | Header strings and settings | Channel names and acquisition representation |
| Instrument metadata | Text and timestamps | Instrument identity and acquisition timing |

**Project applications:** event-level signal analysis, acquisition-quality assessment and interpretation of multichannel measurements.

## Define your dataset

Tell us the scientific task, data types and outcomes your AI needs to learn. We can scope historical-record retrieval, expert annotation, additional measurements and new experimental campaigns with partner scientists. Specimen links, metadata, validation and delivery formats are defined around the project.

**Discuss your data needs:** [mehdi@vicena.ai](mailto:mehdi@vicena.ai) · [vicena.ai/experimental-data](https://vicena.ai/experimental-data)

Updated 10 November 2026.
