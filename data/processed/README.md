# Dataset files

## 📖 Fungi Metadata File Generation

The file `fungi_taxonomy_enriched_v2.csv` was produced through a multi-stage workflow that extracts, normalizes, and enriches fungal species information from the experimental dataset.

### Steps in the Pipeline
1. **Source Data Extraction**
   - Original CSV: `PDF_Extract2 - pdf_extract_2025 (6).csv`
   - Columns used:  
     - `type of fungi`  
     - `any additional information`  

2. **Data Cleaning & Normalization**
   - Standardized species names (e.g., *P. chrysosporium* → *Phanerochaete chrysosporium*).
   - Removed punctuation and harmonized abbreviations.
   - Retained the original raw label in the column `original_fungi_name`.

3. **Enzyme Extraction**
   - Parsed enzyme activities from the `any additional information` column using regex patterns.  
   - Supported enzymes include **laccase, manganese peroxidase (MnP), lignin peroxidase (LiP), versatile peroxidase (VP), cellulase, xylanase,** and others.
   - Results stored in the `enzymes_list` column.

4. **Taxonomy & MycoBank Integration**
   - Species names were mapped to **MycoBank IDs** where available.
   - Added lineage classification in the format:  
     `Kingdom > Phylum > Class > Order > Family > Genus > Species`.

5. **Synonym Resolution**
   - Applied synonym mappings from authoritative fungal taxonomy sources. Examples:  
     - *Coriolus versicolor* → *Trametes versicolor*  
     - *Lentinus edodes* → *Lentinula edodes*  
     - *Polyporus sanguineus* → *Pycnoporus sanguineus*  
   - Introduced two new columns:  
     - `accepted_name`: standardized valid name  
     - `status`: one of **Valid**, **Synonym**, **Genus only**, or **Not available**

   - **`fungi_taxonomy_enriched_v2.csv`** → Final enriched version with synonyms and status flags.

### Example Row

| original_fungi_name | species_name        | accepted_name       | MycoBankID | enzymes_list   | classification | status  |
|----------------------|---------------------|---------------------|------------|----------------|----------------|---------|
| Coriolus versicolor  | Coriolus versicolor | Trametes versicolor | 281625     | Laccase, LiP   | Fungi > …      | Synonym |

---

### ✅ TODOs / Next Steps

- [ ] **Fill missing MycoBank IDs** — many species currently have blank entries.  
- [ ] **Expand taxonomy coverage** — not all genera have complete lineage information.  
- [ ] **Review ambiguous names** — e.g., *White-rot fungi*, *Whole fungi*, *Bjerkandera sp.* should be curated or excluded.  
- [ ] **Confirm synonym mappings** — some taxa (e.g., *Grammothele subargentea* → *Porogramme subargentea*) may need expert confirmation.  
- [ ] **Add enzyme activity values** — right now only enzyme types are listed, but activity levels (U/mL, etc.) could be extracted into structured fields.  
- [ ] **Quality check** — verify that accepted names and classification hierarchies are consistent with the latest MycoBank records.  

---

## 🎨 Dye Metadata File Generation

The file `dye_metadata_enriched_v2.csv` was created to provide structured metadata for all unique dye names identified in the experimental dataset.

### Steps in the Pipeline
1. **Source Data Extraction**
   - Original CSV: `PDF_Extract2 - pdf_extract_2025 (6).csv`
   - Column used:  
     - `type of dye`

2. **Data Cleaning & Normalization**
   - Extracted **268 unique dye names**.  
   - Harmonized capitalization and merged duplicates (e.g., *Reactive blue 19* vs *Reactive Blue 19*).  
   - Preserved the original dye label in the `Dye name` column.

3. **Chemical Metadata Enrichment**
   - **Chemical class** assigned using PubChem, Wikipedia, and ChEBI references.  
   - **Molecular weight (g/mol)** populated where known.  
   - **Structure info** stored as **SMILES** strings for single, well-defined compounds.  
   - Mixtures (e.g., *Basic fuchsin, Methyl violet*) marked as **“Mixture — no single SMILES.”**  
   - Plant extracts (e.g., *Eucalyptus globulus*) marked as **“Natural extract — structure varies.”**

4. **Status Column**
   - Introduced a `status` field to make filtering easier:
     - **Valid** → Defined single compound with MW + SMILES.  
     - **Mixture** → Historical dye blends with no unique SMILES.  
     - **Natural extract** → Plant or crude extract, not a discrete compound.  
     - **Not available** → Metadata could not be found or confirmed.


### Example Row

| Dye name        | Chemical class        | Molecular weight (g/mol) | Structure info | Status  |
|-----------------|-----------------------|--------------------------|----------------|---------|
| Crystal violet  | Triarylmethane dye    | 407.99                   | CN(C)C1=CC=C…  | Valid   |
| Basic fuchsin   | Triarylmethane mixture|                          | Mixture — no… | Mixture |
| Eucalyptus globulus | Natural extract   |                          | Natural extract — structure varies | Natural extract |

---

### ✅ TODOs / Next Steps

- [ ] **Fill missing molecular weights** — many azo/anthraquinone dyes still lack MW.  
- [ ] **Add SMILES for more dyes** where records exist but weren’t mapped yet.  
- [ ] **Refine chemical classes** for food colorants (e.g., Tartrazine, Carmoisine) with CAS numbers.  
- [ ] **Curate ambiguous entries** — plant extracts or misclassified “dyes” may need manual review.  
- [ ] **Cross-check synonyms** (e.g., trade names vs. IUPAC names).  
- [ ] **Expand external IDs** — add PubChem CID or ChEBI ID for database linking.  

---

