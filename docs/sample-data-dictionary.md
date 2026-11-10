# Vicena sample data dictionary

> [Benchmark home](../README.md) · [Benchmark input schema](data-dictionary.md) · [Discuss your data needs](https://vicena.ai/experimental-data)

**Experimental measurements, images, process records and scientific results represented in Vicena's received sample collection.** This dictionary describes the specimens, data types, fields and formats across the collection reviewed on 10 November 2026. It extends beyond the battery and catalyst inputs used in the current benchmark.

The descriptions below follow the supplied files and their inspection records. Field names are readable descriptions; backticked labels identify source fields or channel families. These are not a new common file schema. No source measurements, recipe values, images, supplier identities or answer keys are published here. Sample quantities are outside this dictionary's scope.

## Browse the collection

| Collection | Specimen or observation | Data types | Record form |
| --- | --- | --- | --- |
| [C01 · Battery measurements](#c01--battery-measurements) | Electrolytes, pouch cells and electrode test systems | Formulation, properties, preparation measurements, formation, cycling, impedance, voltammetry and rate response | Numerical workbooks and researcher analysis |
| [C02 · Catalyst characterization](#c02--catalyst-characterization) | Fe–N–C catalyst materials and electrode recordings | Diffraction, electron microscopy, elemental analysis and electrochemical scans | Numerical files, images and reports; broader specification alongside them |
| [C03 · Oxygen electrodes](#c03--oxygen-electrodes) | Composite nanofiber electrodes and a control | Structure, surface chemistry, impedance, polarization and durability | Specification describing the data; acquisitions not included in that document |
| [C04 · Thin films and 2D materials](#c04--thin-films-and-2d-materials) | Patterned structures, transferred graphene and multilayer films | Microscopy, surface topography, height profiles and defect descriptions | Figures and descriptions in a presentation |
| [C05 · Coin-cell process recording](#c05--coin-cell-process-recording) | Laboratory actions, equipment and cell components | Video, process sequence, timestamps and annotations | Recording and supporting documents |
| [C06 · Cell biology and immune assays](#c06--cell-biology-and-immune-assays) | Cell preparations, protein samples and assay conditions | Cytometry, protein images, gene expression, viability, cell damage and immunoassays | Instrument files, image exports, tables and analysis projects |
| [C07 · Immunotherapy results](#c07--immunotherapy-results) | Animal identifiers and treatment groups | Numerical observations and researcher results | Workbook and study figures |
| [C08 · Enzyme kinetics](#c08--enzyme-kinetics) | Wild-type and mutant enzyme under substrate conditions | Kinetic parameters, uncertainty and detection status | Summary table and assay description |
| [C09 · Additional cytometry](#c09--additional-cytometry) | Events within an instrument acquisition | Scatter, fluorescence pulse measurements and acquisition metadata | Native instrument files |

[Other archived materials](#other-archived-materials) cover public reference datasets, model outputs, design files and documents. They are listed separately from these experimental samples.

## Reading the fields

- **Recorded values** are numbers or signals stored in the supplied files. A workbook can contain recorded measurements, formulas and analysis on the same sheet; it is not automatically a native instrument export.
- **Derived values** include normalized responses, fitted parameters, spreadsheet calculations and image-analysis measurements. Keep them linked to their source observations and method.
- **Images and figures** carry pixel data or plotted evidence. An embedded plot does not establish that its underlying numerical array is included.
- **Specifications** describe intended or reported collections. Their method lists do not establish the headers, units or contents of acquisition files.

An unspecified unit remains unspecified. Empty cells, formula errors, absent observations and “not detectable” are distinct states. Events, pixels, cycles, repeated scans and repeated versions of a file are not independent specimens. Cross-file joins require the source's specimen and run mapping; similar labels alone do not establish a matched experiment.

## C01 · Battery measurements

**Specimens:** electrolyte/additive comparisons in NCM622/graphite and LFP/graphite systems, pouch-cell preparation records, and additional LFP, graphite, nickel-rich and silicon-containing electrode test series. **Format:** XLSX.

| Data field or group | Representation / unit | What it records |
| --- | --- | --- |
| Formulation and material labels | Text and categorical labels | Nominal electrolyte, additive and electrode-system identities |
| Ingredient entries and batch quantities | Numbers; source-specific fractions, percentages or mass entries | Recipe tables and batch-mass records; the recording basis varies between tables |
| Electrolyte properties | Numbers; units are not consistently established | Conductivity, moisture and acidity entries associated with formulation labels |
| Cell identity and preparation stage | Text and categorical labels | Named cells and checkpoints such as rest, formation, ageing and grading |
| Preparation masses | Numbers; g where labelled | Mass before filling, after sealing and at degassing/resealing checkpoints; differences may be formulas |
| Checkpoint voltage and impedance | Numbers; V and mΩ in the labelled process table | Recorded electrical measurements at preparation and grading checkpoints |
| Formation and grading capacity | Numbers; mAh | Charge/discharge and grading-capacity measurements, with some unfilled template fields |
| Cycling | Ordered numbers; cycle index and mAh | Discharge capacity along a cycling trace, with temperature and group context |
| Test conditions | Numbers or text; °C, V and C-rate where documented | Temperature, voltage limits and charge/discharge settings; planned settings remain distinct from confirmed execution |
| Rate and resistance tests | Numbers; C-rate, mAh, mΩ and state of charge where labelled | Capacity under different rates and direct-current resistance at stated checkpoints or pulse durations |
| Cyclic voltammetry | Ordered numerical arrays; potential and current | Potential–current traces; use each sheet's axis labels for units and scaling |
| Differential capacity | Ordered numerical arrays; voltage and dQ/dV | Recorded or processed differential-capacity curves; the capacity normalization must follow the source |
| Impedance spectra | Numerical coordinates; source-specific impedance units and sign conventions | Real/imaginary impedance series at labelled states; plotted or shifted series also occur |
| Performance summaries | Numbers and formulas; % or source-defined ratios | Retention, efficiency, normalized capacities and comparisons |
| Researcher interpretation | Text | Conclusions, observations and proposed follow-up work |

**Interpretation:** recipe units are mixed, and some impedance series are transformed for plotting. Preserve those distinctions. Named cell rows support some preparation-to-grading joins; formulation-level cycling labels do not by themselves establish the same-cell link. Repeated sheets and empty fitting templates add no new measurements.

## C02 · Catalyst characterization

**Specimens:** Fe–N–C catalyst samples with electrode/configuration labels. **Formats:** TXT diffraction arrays, JPEG microscopy images, DOCX elemental reports with embedded images, and XLSX electrochemical records.

| Data field or group | Representation / unit | What it records |
| --- | --- | --- |
| Material and electrode labels | Text | Supplied sample, electrode/configuration and test labels |
| Diffraction position | Ordered numbers; unit not declared in the inspected TXT header | The recorded X-ray diffraction scan coordinate; confirm the axis convention before treating it as calibrated 2θ |
| Diffraction intensity | Numbers; instrument scale unspecified | Signal at each scan position; phase assignments are a separate interpretation |
| Scanning electron microscopy (SEM) | Raster pixels and image overlays | Morphology, scale bars and magnification; pixels are image evidence rather than a particle-property table |
| Energy-dispersive X-ray spectroscopy (EDS) | Embedded spectra, maps and tables | Elemental signal and spatial distribution, where included in a report |
| EDS quantification | Element/line labels and numbers; wt%, reported uncertainty and other report-specific fields | Element fractions, line types, k-ratios, apparent concentration and standard information; fields vary by report |
| Electrode potential | Ordered numbers; V | Potential axis in the populated electrochemical exports |
| Current | Signed numbers; A | Current recorded during linear sweeps and multi-cycle cyclic voltammetry |
| Test context | Text and numbers; RPM where supplied | Oxygen-evolution/reduction labels, electrode groups and rotation labels |
| Acquisition sequence | Row order | Order of exported observations; row index is not an elapsed-time measurement |

**Interpretation:** retain the recorded potential reference and current sign. Current is not current density without an electrode area. Folder/filename conflicts, duplicate scan content and an empty workbook need to remain distinguishable from valid specimen joins.

**Companion specification:** a broader metal–nitrogen–carbon catalyst inventory describes iron-, cobalt-, manganese-containing, mixed-metal and phosphorus-modified materials, with diffraction, microscopy and electrochemical tests. Those described families are separate from the Fe–N–C measurement files reviewed here.

## C03 · Oxygen electrodes

**Specimens described:** GDC/PBSCF core–shell nanofiber composites and a PBSCF control, in symmetric-cell and single-cell configurations. **Record form:** DOCX specification. The entries below describe its measurement categories, not inspected acquisition columns.

| Data type described | Expected quantities / representation | Meaning in the specification |
| --- | --- | --- |
| Material and cell context | Composition labels, configuration and preparation context | Composite/control identity and the system being tested |
| Diffraction and electron microscopy | Diffraction traces; SEM and selected transmission electron microscopy (TEM) images | Structure and morphology |
| Elemental analysis | EDS spectra/maps | Element distribution in selected material |
| Surface chemistry | X-ray photoelectron spectroscopy (XPS) spectra | Before/after surface-chemical comparisons |
| Impedance | Electrochemical impedance spectroscopy (EIS) | Response across stated temperatures and operating conditions |
| Polarization | Linear-sweep voltammetry (LSV) | Response in fuel-cell and electrolysis modes |
| Durability | Current versus time | Sustained response during a constant-potential test |

Native formats, units and specimen-to-file mappings belong to the acquisition records. Repeated composition labels in the specification should not be silently resolved into distinct specimens.

## C04 · Thin films and 2D materials

**Specimens:** lithographed patterns, transferred graphene and multilayer films. **Format:** PPTX containing microscopy figures, an atomic force microscopy (AFM) view, a height profile and descriptions.

| Data field or group | Representation / unit | What it records |
| --- | --- | --- |
| Pattern appearance | Raster figure; scale annotation where shown | Edges, linewidth variation and visible pattern defects |
| Surface topography | AFM figure with its displayed axes/scale | Surface features associated with a graphene-transfer example |
| Height profile | Plotted distance–height relationship | The profile shown beside the AFM image; native profile values are not established by the plot |
| Film morphology | Raster figure | Wrinkles, breaks or damage described in the example |
| Researcher description | Text | Reported process context and interpretation of the figure |

**Interpretation:** these are illustrated outcomes, not complete process logs or native AFM arrays. A reported defect is not an independently established cause. The figures do not constitute a new unpublished measurement collection.

## C05 · Coin-cell process recording

**Observations:** electrode preparation, coating, assembly, equipment handling and testing context. **Formats:** MP4, XLSX moment/annotation records and PDF supporting material.

| Data field or group | Representation / unit | What it records |
| --- | --- | --- |
| Video frames | Time-ordered image sequence | Visible laboratory actions, tools, components and equipment |
| Time reference | Video timestamp or annotation position | Where an observation appears in the recording |
| Process stages | Text and sequence | Preparation, coating, assembly and test-loading context |
| Moment annotations | Text associated with video positions | Descriptions of visible actions and objects |
| Laboratory context | Supporting text | Explanations and clarifications accompanying the recording |
| Demonstration annotations | Separately authored tags/overlays | Later presentation and feature-extraction layers, including AI-assisted tags |

**Interpretation:** the original recording and later edited demonstrations are distinct. Generated tags are not measured laboratory signals or independently verified labels. The cycling result discussed in the recording concerns an earlier cell; it is not the measured outcome of the filmed assembly. Video is an optional process-data modality.

## C06 · Cell biology and immune assays

**Specimens:** glioma-related cell preparations and cellular/immune-response comparisons, including astrocyte, microglial, macrophage and T-cell contexts. **Formats:** FCS, TIFF, XLSX and GraphPad Prism projects, with study documents.

| Data field or group | Representation / unit | What it records |
| --- | --- | --- |
| Cytometry events | Floating-point event-by-channel arrays | Individual acquisition events; scatter and fluorescence pulse measurements |
| Scatter and fluorescence channels | Header-defined signal scales | Forward/side scatter and labelled fluorescence channels; pulse area, height and width where recorded |
| Acquisition metadata | Text, dates/times and parameter definitions | Instrument, acquisition timing, channel labels, numeric representation and byte order |
| Protein-image exports | TIFF pixels | Chemiluminescent, colorimetric and composite views; these views can represent the same acquisition group |
| Protein quantification | Numbers and formulas; source signal units and dimensionless ratios | Band/intensity summaries, control normalization and calculated relative signals |
| Gene-expression tables | Numbers; cycle-threshold values and calculated ratios | Target/reference readings, ΔCt, ΔΔCt and relative expression calculations |
| Viability | Numbers indexed by condition and observation point | CCK-8 response tables; verify the reader scale and time units from the source context |
| Cell-damage assay | Optical density and calculated activity; U/mL where labelled | LDH standards, sample readings and researcher conversions |
| Immunoassay calibration | Optical density and standard concentrations | Calibration and sample-response tables for ELISA measurements |
| Protein/cytokine concentrations | Numbers; pg/mL or ng/mL as labelled | MIF, LGALS1 and IFNG assay results; units differ by analyte |
| Immune-response summaries | Numbers and condition labels | Marker, proliferation and T-cell response summaries; retain each assay's measurement definition |
| Statistical analysis | Prism project structures and researcher figures | Analysis state, tabulated results and presentation layers |

**Interpretation:** native cytometry, image exports and spreadsheet-derived results have different provenance. Do not infer native qPCR or plate-reader files from a result table, or assume a shared specimen across assays without a mapping. Time/channel units and gating context must follow the acquisition rather than an assumed convention.

## C07 · Immunotherapy results

**Observations:** animal-level entries grouped by treatment. **Formats:** XLSX, presentation figures and a study document.

| Data field or group | Representation / unit | What it records |
| --- | --- | --- |
| Animal identifier | Identifier stored as a number | The recorded row identity within a sheet |
| Treatment group | Text | Assigned group label as written on that sheet |
| Numerical observations | Numbers or empty cells; units unspecified | Unheaded result columns; their physical meaning must not be inferred from the values |
| Result summary | Number or formula; units unspecified | A separate result column, including a researcher-calculated entry |
| Study figures and context | Figures and prose | The accompanying interpretation and study description |

**Interpretation:** some treatment labels differ between sheets. The dictionary preserves that ambiguity; it does not relabel observations or assign an unconfirmed endpoint such as volume, mass or survival time.

## C08 · Enzyme kinetics

**Specimens:** an L-aspartate β-decarboxylase, its wild-type and double-mutant forms, and substrate comparisons. **Format:** DOCX with a kinetic-results table and assay context.

| Data field | Representation / unit | What it records |
| --- | --- | --- |
| Enzyme variant | Categorical label | Wild-type or mutant identity |
| Substrate | Categorical label | The substrate condition associated with a result |
| `Km` | Number with reported ± term; mM | Reported Michaelis constant |
| `kcat` | Number with reported ± term; s⁻¹ | Reported turnover parameter |
| `kcat/Km` | Number; mM⁻¹·s⁻¹ | Reported catalytic efficiency |
| Detection status | Text, including `ND` | “Not detectable”; it is not a numerical zero |
| Assay and analysis context | Text | Product detection by high-performance liquid chromatography (HPLC) and the stated analysis method |

**Interpretation:** these are reported fitted summaries. The document does not supply native chromatograms or the full substrate–response series. The meaning of the ± terms is not independently established by the table.

## C09 · Additional cytometry

**Observation unit:** an event within an Attune NxT acquisition; biological specimen context is not established by the inspected headers. **Format:** FCS 3.1.

| Data field or group | Representation / unit | What it records |
| --- | --- | --- |
| Event identifier | Numeric event field | Ordering/identity within the acquisition |
| `Time` | Number; header-defined scale | Acquisition timing coordinate, not an assumed duration in seconds |
| `FSC` / `SSC` | Floating-point pulse measurements | Forward/side scatter area, height and width where recorded |
| Fluorescence channels | Floating-point pulse measurements | Recorded BL/YL channels with area, height and width variants |
| Parameter definitions | Header strings and numeric settings | Channel names and acquisition representation |
| Instrument and timing metadata | Text and timestamps | Instrument identification and acquisition times |

**Interpretation:** fluorescence channel names do not establish a biomarker identity, gate, phenotype or independent reference label. Events within one file share acquisition context.

## Other archived materials

These holdings complete the archive map. They are reference, documentary or computational material rather than additional private laboratory acquisitions.

| Holding | Data types and structure | Record form |
| --- | --- | --- |
| Semiconductor process reference data | Unnamed numerical feature columns, missing-value markers, outcome labels and timestamps | SECOM text data and description files; public/reference collection |
| Organoid assay reference data | Tissue-labelled worksheets, viability/ATP and caspase assay context, controls and time-point summaries | TransQST XLSX reference workbook |
| Nuclei image reference collection | Image pixels, annotation JSON and foreground/background class mappings | JPEG/PNG, JSON and CSV; transformed reference collection |
| Battery market reference tables | Country/category labels and chart-series values | CSV market/reference tables; not cell-test measurements |
| Life-cycle assessment exports | Process/product labels, inventory/impact categories, units, model settings and calculated totals | SimaPro-derived XLSX tables and analysis figures |
| Engineering design and simulation packages | CAD/mesh geometry, solver configuration, calculated fields and technical drawings | Engineering archives; not measured physical outcomes |
| Theses, papers and review packages | Manuscript text, tables, figures, literature and supplementary documents | DOCX/PDF and associated archives; not presumed to contain native acquisitions |
| Edited scientific demonstration media | Video, narration and separately authored visual/feature annotations | Presentation derivatives, including AI-assisted layers |
| Proposals and buyer requests | Requested data types, proposed scopes and commercial descriptions | Documents describing work, not experimental observations |

## Using this dictionary

Choose a collection and the observation you want an AI to interpret or predict. The [benchmark input schema](data-dictionary.md) describes the narrower, frozen battery/catalyst interface already used in the pilot; the other collections here have not thereby become benchmark tasks.

For a data project, agree the specimen/run mapping, measurement formats, required context, expert interpretation and independent outcomes. Historical records can be supplemented through scientist-led record recovery, separate annotations and new measurements; new work remains identifiable as new work. [Discuss the data you need with Vicena](https://vicena.ai/experimental-data).
