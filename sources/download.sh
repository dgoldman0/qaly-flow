#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
PDFDIR="$DIR/pdfs"
mkdir -p "$PDFDIR"
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36'

declare -A URLS=(
  [sanders2016_second_panel.pdf]="https://eprints.whiterose.ac.uk/110276/7/jsc160017_1.pdf"
  [russell1996_role_cea.pdf]="https://jamanetwork.com/journals/jama/articlepdf/403829/jcv60006.pdf"
  [weinstein2009_qalys_basics.pdf]="https://www.ispor.org/docs/default-source/health-policy/101101_qalysbasics.pdf"
  [attema2018_discounting.pdf]="https://eprints.whiterose.ac.uk/137481/3/Discounting_in_economic_evaluations.pdf"
  [lakdawalla2018_elements_value.pdf]="https://www.valueinhealthjournal.com/article/S1098-3015(17)33892-5/pdf?download=true"
  [lakdawalla2015_insurance_value_nber.pdf]="https://www.nber.org/system/files/working_papers/w21015/w21015.pdf"
  [asaria2015_dcea_tutorial.pdf]="https://www.york.ac.uk/media/che/documents/papers/researchpapers/CHERP116.pdf"
  [cookson2021_dcea_comes_of_age.pdf]="https://eprints.whiterose.ac.uk/169332/1/DCEAcomesofageSubmitted.pdf"
  [pickard2019_eq5d5l_us.pdf]="https://euroqol.org/wp-content/uploads/2020/10/Pickard_et_al-2019-Medical_Care.pdf"
  [nice_dsu_tsd11.pdf]="https://www.sheffield.ac.uk/media/34094/download?attachment"
  [nice_dsu_tsd15.pdf]="https://www.sheffield.ac.uk/media/34206/download?attachment"
  [sigman_rrt.pdf]="https://www.columbia.edu/~ks20/stochastic-I/stochastic-I-RRT.pdf"
  [sigman_regenerative.pdf]="https://www.columbia.edu/~ks20/stochastic-I/stochastic-I-Regenerative.pdf"
  [kallenberg_mdp_notes.pdf]="https://pub.math.leidenuniv.nl/~spieksmafm/colleges/LNMB-MDP/Lecture-notes-Kallenberg.pdf"
  [wan2021_avg_reward_mdp.pdf]="https://proceedings.mlr.press/v139/wan21a/wan21a.pdf"
  [subramanian2020_renewal_monte_carlo.pdf]="https://adityam.github.io/files/projects/reinforcement-learning/journal/2020-renewal-monte-carlo.pdf"
  [pitman2012_dynamic_transmission.pdf]="https://www.ispor.org/docs/default-source/practice-policy/dynamic_transmission_modeling-5.pdf"
  [ultsch2015_vaccine_framework.pdf]="https://edoc.rki.de/bitstream/handle/176904/2152/21yHRUNVIxKw.pdf?isAllowed=y&sequence=1"
  [ta2024_pcv20_germany.pdf]="https://link.springer.com/content/pdf/10.1007/s40121-024-00977-4.pdf"
  [goulionis2010_diabetic_foot.pdf]="https://www.dovepress.com/getfile.php?fileID=5051"
  [bauerreif2025_health_risk_value_of_life.pdf]="https://julianreif.com/research/reif.jpube.2025.healthrisk.pdf"
  [masny2023_healthspan_extension.pdf]="https://michalmasny.com/resources/Masny-HealthspanExtension.pdf"
  [utkus2025_extending_healthspans.pdf]="https://www.nber.org/system/files/working_papers/w33992/w33992.pdf"
  [omahony2015_dealing_with_time.pdf]="https://repub.eur.nl/pub/78761/10.1007s40273-015-0309-4_OA.pdf"
  [scott2021_targeting_aging.pdf]="https://www.nature.com/articles/s43587-021-00080-0.pdf"
  [scott2022_international_gains_healthy_longevity.pdf]="https://perspectivesinmedicine.cshlp.org/content/12/9/a041258.full.pdf"
)

failures=0
for f in "${!URLS[@]}"; do
  url="${URLS[$f]}"
  out="$PDFDIR/$f"
  echo "Downloading $f"
  # -L follow redirects, --retry for robustness
  if ! curl -L --fail --retry 3 --retry-delay 2 -A "$UA" -o "$out" "$url"; then
    echo "FAILED: $f <- $url" >&2
    rm -f "$out"
    failures=$((failures+1))
  fi
  # sanity check: ensure it looks like a PDF
  if [ -f "$out" ]; then
    headbytes=$(head -c 4 "$out" || true)
    if [ "$headbytes" != "%PDF" ]; then
      echo "NOT A PDF (header $headbytes): $f" >&2
      rm -f "$out"
      failures=$((failures+1))
    fi
  fi
done

echo "Failures: $failures"
if [ $failures -ne 0 ]; then
  echo "Some downloads failed." >&2
  exit 2
fi
