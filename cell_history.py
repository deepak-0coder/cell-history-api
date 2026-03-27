from dataclasses import dataclass
from typing import List

@dataclass
class Milestone:
    year: int
    scientist: str
    discovery: str
    category: str  # "Structural" or "Functional"
    location: str

def get_data() -> List[Milestone]:
    return [
        Milestone(1665, "Robert Hooke", "Observed 'cells' in cork", "Structural", "England"),
        Milestone(1674, "Leeuwenhoek", "Observed 'animalcules' (bacteria)", "Structural", "Netherlands"),
        Milestone(1831, "Robert Brown", "Identified the nucleus", "Structural", "England"),
        Milestone(1839, "Schleiden & Schwann", "Cell Theory: Basic unit of life", "Functional", "Germany"),
        Milestone(1858, "Rudolf Virchow", "Cells come from cells", "Functional", "Germany"),
        Milestone(1953, "Watson & Crick", "DNA Double Helix structure", "Structural", "England"),
        Milestone(2012, "Doudna & Charpentier", "CRISPR Gene Editing", "Functional", "USA/France")
    ]

def main():
    history = get_data()
    print("🔬 CELL BIOLOGY HISTORY ENGINE v2.0")
    print("-" * 40)
    
    # Example Function: Filter by Category
    print("\n[QUERY] Show all 'Functional' milestones:")
    for m in history:
        if m.category == "Functional":
            print(f"-> {m.year}: {m.discovery} ({m.scientist})")

    # Example Function: Stats
    structural_count = len([m for m in history if m.category == "Structural"])
    print(f"\n[STATS] Total Structural Milestones: {structural_count}")

if __name__ == "__main__":
    main()
