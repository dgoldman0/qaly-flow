# Changelog

All notable changes to this project will be documented in this file.

## [2026-01-30] - Symbol Normalization Fix and Scoped Training Mode

### Added
- **New training mode: `training_scoped.jsonl`**
  - Only includes full answers for questions with maximum confidence (⬤⬤⬤) AND maximum consistency (⬤⬤⬤) after normalization
  - Lower quality questions receive only preamble responses
  - System message includes: "You are in hard-scoped mode. Respond only with a preamble message for out of scope questions."
  
- **Merged JSONL files**
  - Created `qalyflow.jsonl` by concatenating `snippets.jsonl`, `sources.jsonl`, and `training_prose.jsonl`

### Fixed
- **Symbol normalization bug in `generate.py`**
  - Added support for additional unicode symbols: `⬘` (filled), various block characters
  - Fixed mapping between different unicode representations of the same symbol patterns
  - Updated `normalize_symbols()` to preserve character order while standardizing symbols
  
- **Preamble matching issues**
  - Updated `load_preambles()` to store both original and normalized symbol keys
  - Fixed exact equality checks that were failing due to unicode character differences
  
- **CSV alignment issues**
  - Fixed scoped mode to use CSV questions instead of internal array questions to ensure alignment with confidence/consistency ratings
  - Refactored `build_training_example()` to accept answer as parameter instead of extracting from question_data
  
- **Preamble-only logic**
  - Fixed conditional logic in `build_training_example()` to properly handle cases where only preamble should be included
  - Added `elif preamble:` branch to use preamble when answer is empty

### Changed
- **Function signatures**
  - `build_training_example()` now takes `answer` as direct parameter instead of `question_data` dict
  - Simplified answer extraction logic in `generate_jsonl()`

### Technical Details
- Symbol normalization now handles: `⬤`, `●`, `█`, `■`, `▆`, `▇`, `▉`, `▊`, `▋`, `⬘` → `⬤`
- Empty symbols: `◯`, `○`, `░`, `□`, `▁`, `▂`, `▃`, `▄`, `▅` → `◯`
- High quality threshold: confidence=`⬤⬤⬤` AND consistency=`⬤⬤⬤` (after normalization)

### Output Statistics
- `training_prose.jsonl`: 360/360 questions included
- `training_symbolic.jsonl`: 172/360 questions included (188 skipped for empty symbolic answers)  
- `training_scoped.jsonl`: 360/360 questions included (with conditional full answers based on quality ratings)