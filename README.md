# cell-history-api
About the history of cell\
"""
History of Cell Biology: From 1665 to Present
A comprehensive timeline and educational resource
"""

from dataclasses import dataclass
from typing import List
from datetime import datetime

@dataclass
class CellDiscovery:
    """Represents a major discovery or milestone in cell biology"""
    year: int
    scientist: str
    discovery: str
    significance: str
    location: str = "Unknown"

class CellHistoryTimeline:
    """Manages and displays the history of cell discoveries"""
    
    def __init__(self):
        self.discoveries: List[CellDiscovery] = []
        self._populate_discoveries()
    
    def _populate_discoveries(self):
        """Populate the timeline with major cell biology discoveries"""
        
        self.discoveries = [
            CellDiscovery(
                year=1665,
                scientist="Robert Hooke",
                discovery="First observation of 'cells' in cork tissue",
                significance="Named cellular structures; foundation of cell biology",
                location="England"
            ),
            CellDiscovery(
                year=1674,
                scientist="Antonie van Leeuwenhoek",
                discovery="Observed microscopic organisms (protozoa and bacteria)",
                significance="Revealed the existence of unicellular organisms",
                location="Netherlands"
            ),
            CellDiscovery(
                year=1804,
                scientist="Jean-Baptiste Lamarck",
                discovery="Proposed cells are basic unit of life",
                significance="Early cell theory foundation",
                location="France"
            ),
            CellDiscovery(
                year=1831,
                scientist="Robert Brown",
                discovery="Identified the cell nucleus in orchids",
                significance="Revealed nucleus as cell's central organelle",
                location="England"
            ),
            CellDiscovery(
                year=1839,
                scientist="Matthias Schleiden & Theodor Schwann",
                discovery="Formulated Cell Theory (cells come from cells)",
                significance="Established that all organisms are made of cells",
                location="Germany"
            ),
            CellDiscovery(
                year=1858,
                scientist="Rudolf Virchow",
                discovery="'Omnis cellula e cellula' (all cells from cells)",
                significance="Completed the basic cell theory",
                location="Germany"
            ),
            CellDiscovery(
                year=1880,
                scientist="Various scientists",
                discovery="Identification of organelles (mitochondria, chloroplasts)",
                significance="Understanding of cellular compartmentalization",
                location="Multiple"
            ),
            CellDiscovery(
                year=1898,
                scientist="Camillo Golgi",
                discovery="Identified the Golgi apparatus",
                significance="Revealed protein processing and packaging organelle",
                location="Italy"
            ),
            CellDiscovery(
                year=1902,
                scientist="Sutton & Boveri",
                discovery="Chromosomal theory of inheritance",
                significance="Linked genes to physical structures in cells",
                location="USA & Germany"
            ),
            CellDiscovery(
                year=1944,
                scientist="Oswald Avery",
                discovery="DNA identified as genetic material",
                significance="Foundation for molecular biology",
                location="USA"
            ),
            CellDiscovery(
                year=1950,
                scientist="Erwin Chargaff",
                discovery="Chargaff's rules for DNA composition",
                significance="Led to understanding DNA structure",
                location="USA"
            ),
            CellDiscovery(
                year=1953,
                scientist="Watson, Crick, Franklin & Wilkins",
                discovery="DNA double helix structure revealed",
                significance="Revolutionized understanding of genetic information storage",
                location="England"
            ),
            CellDiscovery(
                year=1956,
                scientist="George Palade",
                discovery="Ribosomes and rough endoplasmic reticulum",
                significance="Understanding protein synthesis",
                location="USA"
            ),
            CellDiscovery(
                year=1970,
                scientist="Lynn Margulis",
                discovery="Endosymbiotic theory refined",
                significance="Explained origin of mitochondria and chloroplasts",
                location="USA"
            ),
            CellDiscovery(
                year=1982,
                scientist="Aaron Klug",
                discovery="3D structure of chromatin",
                significance="Understanding DNA packaging in nucleus",
                location="England"
            ),
            CellDiscovery(
                year=1990,
                scientist="Various scientists",
                discovery="Human Genome Project initiated",
                significance="Mapping all human genes",
                location="International"
            ),
            CellDiscovery(
                year=2003,
                scientist="International consortium",
                discovery="Human Genome Project completed",
                significance="Complete map of human genetic code",
                location="International"
            ),
            CellDiscovery(
                year=2006,
                scientist="Shinya Yamanaka",
                discovery="Induced Pluripotent Stem Cells (iPSCs)",
                significance="Cell reprogramming breakthrough",
                location="Japan"
            ),
            CellDiscovery(
                year=2012,
                scientist="Jennifer Doudna & Emmanuelle Charpentier",
                discovery="CRISPR-Cas9 gene editing refined",
                significance="Revolutionary gene editing technology",
                location="USA & France"
            ),
            CellDiscovery(
                year=2020,
                scientist="Multiple research teams",
                discovery="Single-cell RNA sequencing advances",
                significance="Understanding cell heterogeneity at molecular level",
                location="International"
            ),
            CellDiscovery(
                year=2024,
                scientist="Ongoing research",
                discovery="Artificial cells and synthetic biology",
                significance="Creating cells from non-living materials",
                location="International"
            ),
        ]
    
    def display_timeline(self):
        """Display the complete timeline"""
        print("=" * 80)
        print("HISTORY OF CELL BIOLOGY: 1665 - PRESENT")
        print("=" * 80)
        print()
        
        for discovery in self.discoveries:
            print(f"📅 YEAR: {discovery.year}")
            print(f"👤 Scientist(s): {discovery.scientist}")
            print(f"🔬 Discovery: {discovery.discovery}")
            print(f"⭐ Significance: {discovery.significance}")
            print(f"📍 Location: {discovery.location}")
            print("-" * 80)
            print()
    
    def get_discoveries_by_century(self, century: int) -> List[CellDiscovery]:
        """Get discoveries from a specific century (e.g., 17 for 17th century)"""
        start_year = (century - 1) * 100 + 1
        end_year = century * 100
        
        return [d for d in self.discoveries if start_year <= d.year <= end_year]
    
    def get_discoveries_by_scientist(self, scientist_name: str) -> List[CellDiscovery]:
        """Get all discoveries by a specific scientist"""
        return [d for d in self.discoveries if scientist_name.lower() in d.scientist.lower()]
    
    def get_discoveries_by_year_range(self, start: int, end: int) -> List[CellDiscovery]:
        """Get discoveries within a year range"""
        return [d for d in self.discoveries if start <= d.year <= end]
    
    def print_century_summary(self, century: int):
        """Print summary of discoveries in a century"""
        discoveries = self.get_discoveries_by_century(century)
        print(f"\n{'=' * 80}")
        print(f"DISCOVERIES IN THE {century}{'th' if century % 100 != 11 else 'st' if century % 100 == 1 else 'nd' if century % 100 == 2 else 'rd' if century % 100 == 3 else 'th'} CENTURY")
        print(f"{'=' * 80}\n")
        
        if not discoveries:
            print(f"No major discoveries recorded for this century.")
            return
        
        for discovery in discoveries:
            print(f"  {discovery.year}: {discovery.discovery}")
            print(f"           By: {discovery.scientist}\n")
    
    def get_statistics(self):
        """Get statistics about the timeline"""
        print(f"\n{'=' * 80}")
        print("STATISTICS")
        print(f"{'=' * 80}")
        print(f"Total Discoveries/Milestones: {len(self.discoveries)}")
        print(f"Time Span: {self.discoveries[0].year} - {self.discoveries[-1].year}")
        print(f"Number of Years: {self.discoveries[-1].year - self.discoveries[0].year + 1}")
        
        # Count discoveries by century
        centuries = {}
        for discovery in self.discoveries:
            century = (discovery.year - 1) // 100 + 1
            centuries[century] = centuries.get(century, 0) + 1
        
        print(f"\nDiscoveries by Century:")
        for century in sorted(centuries.keys()):
            print(f"  {century}th Century: {centuries[century]} discoveries")


def main():
    """Main function to run the cell history application"""
    
    timeline = CellHistoryTimeline()
    
    # Display full timeline
    timeline.display_timeline()
    
    # Display statistics
    timeline.get_statistics()
    
    # Example: Show discoveries in specific centuries
    print("\n" + "=" * 80)
    print("CENTURY SUMMARIES")
    print("=" * 80)
    
    for century in [17, 18, 19, 20, 21]:
        timeline.print_century_summary(century)
    
    # Example: Search by scientist
    print("\n" + "=" * 80)
    print("SEARCH EXAMPLES")
    print("=" * 80)
    
    print("\nDiscoveries by Robert Hooke:")
    hooke_discoveries = timeline.get_discoveries_by_scientist("Robert Hooke")
    for d in hooke_discoveries:
        print(f"  {d.year}: {d.discovery}")
    
    print("\nDiscoveries in 20th Century:")
    century_20 = timeline.get_discoveries_by_century(20)
    for d in century_20:
        print(f"  {d.year}: {d.discovery} - {d.scientist}")


if __name__ == "__main__":
    main()
