from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
# Create a new instance of the Chrome self.webdriver
class Driver:
    def __init__(self, pdb_id: str) -> None:
        self.webdriver = webdriver.Chrome()
        self.pdb_id = pdb_id
        self.rnapdbeurl = "http://rnapdbee.cs.put.poznan.pl/"

    def get_all_annotations(self):
        annotations =  {"RNAVIEW": self.getRNAVIEWannoations(),
                        "MCAnnotate": self.getMCAnnotations(),
                        "3DNA": self.get_3DNA_annotations(),
                    #    "FR3D": self.get_FR3D_annotations()
                    # FR3D has a differnet format and I am not sure it even gives base pair annotations
                        }
        self.webdriver.quit()
        return annotations
    
    def getMCAnnotations(self):
        # Open a website
        self.webdriver.get(self.rnapdbeurl)

        mc_annotate_button = WebDriverWait(self.webdriver, 10).until(
            EC.element_to_be_clickable((By.ID, "mcannotate"))
        )
        mc_annotate_button.click()
        return self._runRNApdbee()
    
    def getRNAVIEWannoations(self):
        self.webdriver.get(self.rnapdbeurl)
        rna_view_button = WebDriverWait(self.webdriver, 10).until(
            EC.element_to_be_clickable((By.ID, "rnaview"))
        )

        rna_view_button.click()
        return self._runRNApdbee()
    

    def get_3DNA_annotations(self):
        self.webdriver.get(self.rnapdbeurl)

        three_dna_button = WebDriverWait(self.webdriver, 10).until(
            EC.element_to_be_clickable((By.ID, "dssr"))
        )
        three_dna_button.click()
        return self._runRNApdbee()
    
    def get_FR3D_annotations(self):
        self.webdriver.get(self.rnapdbeurl)

        FR3D_button = WebDriverWait(self.webdriver, 10).until(
            EC.element_to_be_clickable((By.ID, "fr3d"))
        )
        FR3D_button.click()
        return self._runRNApdbee()
    

    
    def _runRNApdbee(self):
        show_noncanonical_basepairs_button = WebDriverWait(self.webdriver, 10).until(
            EC.element_to_be_clickable((By.ID, "nonCanonicalHandling2"))
        )

        show_noncanonical_basepairs_button.click()


        self.webdriver.find_element(By.ID, "pdbId").send_keys(self.pdb_id)

        get_pdb_file_button = WebDriverWait(self.webdriver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Get']"))
        )
        get_pdb_file_button.click()  

        submit_button = WebDriverWait(self.webdriver, 10).until(
            EC.element_to_be_clickable((By.ID, "commitPdb"))
        )
        submit_button.click()

        #wait for page with annotations to load
        WebDriverWait(self.webdriver, 10).until(
            EC.presence_of_element_located((By.ID, "showhidePdbReanalyzeForm"))
        )

        return self.webdriver.page_source