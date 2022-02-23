"""Pandas import of the RMRIO database."""

import h5py
import mat73
import pandas as pd

from scipy import sparse

class rmrio_import():
    """Import RMRIO database."""

    def __init__(
            self,
            rmrio_file_path = "rmrio-data/",
            rmrio_year = 2015
            ):
        """Init.
        
        (Optional) Specify path to the RMRIO database files and the RMRIO
        database year.
        
        Parameters
        ----------
        rmrio_file_path : STRING, optional
            DESCRIPTION. The default is "rmrio-data/".
        rmrio_year : INT, optional
            DESCRIPTION. The default is 2015.

        """
        self.rmrio_file_path = rmrio_file_path
        self.rmrio_year = rmrio_year
        
# =============================================================================
#       Labels   
# =============================================================================
        
        # 189 regions

        self.region_idx = mat73.loadmat(
            f"{self.rmrio_file_path}/"
            "Labels_RMRIO/Labels_RMRIO/Labels_Countries_RMRIO.mat"
            )
        
        self.region_idx = pd.Series(
            [i[0] for i in self.region_idx["Labels_Countries_RMRIO"]],
            name ="region"
            )
        
        # 163 sectors
        
        self.sector_idx = mat73.loadmat(
            f"{self.rmrio_file_path}/"
            "Labels_RMRIO/Labels_RMRIO/Labels_Sectors_RMRIO.mat"
            )
        
        self.sector_idx = pd.Series(
            [i[0] for i in self.sector_idx["Labels_Sectors_RMRIO"]],
            name ="sector"
            )
        
        # 9 extensions
        self.extension_idx = mat73.loadmat(
            f"{self.rmrio_file_path}/"
            "Labels_RMRIO/Labels_RMRIO/Labels_Extensions_RMRIO.mat"
            )
        
        self.extension_idx = pd.Series(
            [i[0] for i in self.extension_idx["Labels_Extensions_RMRIO"]],
            name ="extension"
            )
        
        # 6 final demand categories * 189 regions = 1134 (region, fd category)
        
        self.y_idx = mat73.loadmat(
            f"{self.rmrio_file_path}/"
            "Labels_RMRIO/Labels_RMRIO/Labels_FinalDemand_RMRIO.mat"
            )
        
        self.y_idx = pd.DataFrame.from_dict(
            self.y_idx["Labels_FinalDemand_RMRIO"]
            )
        
        self.y_idx.columns = ["region","category"]
        
        # 189 regions * 163 sectors = 30807 (region,sector)
        
        self.idx = mat73.loadmat(
            f"{self.rmrio_file_path}/"
            "Labels_RMRIO/Labels_RMRIO/Labels_Production_RMRIO.mat"
            )
        
        self.idx = pd.DataFrame.from_dict(
            self.idx["Labels_Production_RMRIO"]
            )
        
        self.idx.columns = ["region","sector"]
        
# =============================================================================
#   Database elements
# =============================================================================
        
    def import_x(self):
        """
        Import x.
        
        Import the total output (transactions + final demand).
        
        Rows: 189 regions * 163 sectors = 30807 (region,sector)

        Returns
        -------
        RMRIO_TotalOut : pd.Series
            The sectors' total output.

        """
        print("Importing the total output ...")
        f = h5py.File(
            f"{self.rmrio_file_path}/"
            f"Year_{self.rmrio_year}_RMRIO/"
            f"Year_{self.rmrio_year}_RMRIO/TotalOut_RMRIO.mat"
            )
        
        RMRIO_TotalOut = sparse.csc_matrix(
            (
             f["TotalOut_RMRIO/data"],
             f["TotalOut_RMRIO/ir"],
             f["TotalOut_RMRIO/jc"]
             )
            )
        
        RMRIO_TotalOut = RMRIO_TotalOut.toarray()
        
        RMRIO_TotalOut = pd.Series(
            RMRIO_TotalOut.flatten(),
            name = "x"
            )
        
        # Add index
        
        RMRIO_TotalOut.index = pd.MultiIndex.from_frame(
            self.idx
            )
        
        return RMRIO_TotalOut
        
    def import_Y(self):
        """
        Import Y.
        
        Import the final demand.
        
        Rows: 189 regions * 163 sectors = 30807 (region,sector)
        Columns: 6 FD categories * 189 regions = 1134 (region, fd category)

        Returns
        -------
        RMRIO_Y : pd.DataFrame
            The final demand from the sectors.

        """
        print("Importing the final demand ...")

        f = h5py.File(
            f"{self.rmrio_file_path}/"
            f"Year_{self.rmrio_year}_RMRIO/"
            f"Year_{self.rmrio_year}_RMRIO/Y_RMRIO.mat"
            )
        
        RMRIO_Y = sparse.csc_matrix(
            (
             f["Y_RMRIO/data"],
             f["Y_RMRIO/ir"],
             f["Y_RMRIO/jc"]
             )
            )
        
        RMRIO_Y = RMRIO_Y.toarray()
        
        RMRIO_Y = pd.DataFrame(RMRIO_Y)
        
        # Add index
        
        RMRIO_Y.columns = pd.MultiIndex.from_frame(
            self.y_idx,
            )
        
        RMRIO_Y.index = pd.MultiIndex.from_frame(
            self.idx,
            )

        return RMRIO_Y
    
    def import_extensions_hh(self):
        """
        Import the households' extensions.
        
        Rows: 9 extensions
        Columns: 6 FD categories * 189 regions = 1134 (region, fd category)

        Returns
        -------
        RMRIO_Ext_hh : pd.DataFrame
            The household's extensions.

        """
        print("Importing the households' extensions ...")

        
        f = h5py.File(
            f"{self.rmrio_file_path}/"
            f"Year_{self.rmrio_year}_RMRIO/"
            f"Year_{self.rmrio_year}_RMRIO/Ext_hh_RMRIO.mat"
            )
        
        RMRIO_Ext_hh = sparse.csc_matrix(
            (
             f["Ext_hh_RMRIO/data"],
             f["Ext_hh_RMRIO/ir"],
             f["Ext_hh_RMRIO/jc"]
             )
            )
        
        RMRIO_Ext_hh = RMRIO_Ext_hh.toarray()
        
        RMRIO_Ext_hh = pd.DataFrame(RMRIO_Ext_hh)
        
        # Add index
        
        RMRIO_Ext_hh.columns = pd.MultiIndex.from_frame(
            self.y_idx
            )
        
        RMRIO_Ext_hh.index = self.extension_idx
            
        return RMRIO_Ext_hh
    
    def import_extensions(self):
        """
        Import the sectors' extensions.
        
        # Rows: 9 extensions
        # Columns: 189 regions * 163 sectors = 30807 (region,sector)

        Returns
        -------
        RMRIO_Ext : pd.DataFrame
            The sectors' extensions.

        """
        print("Importing the sectors' extensions ...")
        
        f = h5py.File(
            f"{self.rmrio_file_path}/"
            f"Year_{self.rmrio_year}_RMRIO/"
            f"Year_{self.rmrio_year}_RMRIO/Ext_RMRIO.mat"
            )
        
        RMRIO_Ext = sparse.csc_matrix(
            (
             f["Ext_RMRIO/data"],
             f["Ext_RMRIO/ir"],
             f["Ext_RMRIO/jc"]
             )
            )
        
        RMRIO_Ext = RMRIO_Ext.toarray()
        
        RMRIO_Ext = pd.DataFrame(RMRIO_Ext)
        
        # Add index
        
        RMRIO_Ext.columns = pd.MultiIndex.from_frame(
            self.idx
            )
        
        RMRIO_Ext.index = self.extension_idx
            
        return RMRIO_Ext
    
    def import_A(self):
        """
        Import the technical coefficients.
        
        Rows: 189 regions * 163 sectors = 30807 (region,sector)
        Columns: 189 regions * 163 sectors = 30807 (region,sector)

        Returns
        -------
        RMRIO_A : pd.DataFrame
            The technical coefficients.

        """
        print("Importing the technical coefficients ...")
        
        f = h5py.File(
            f"{self.rmrio_file_path}/"
            f"Year_{self.rmrio_year}_RMRIO/"
            f"Year_{self.rmrio_year}_RMRIO/A_RMRIO.mat"
            )
        
        RMRIO_A = sparse.csc_matrix(
            (
             f["A_RMRIO/data"],
             f["A_RMRIO/ir"],
             f["A_RMRIO/jc"]
             )
            )
        
        RMRIO_A = RMRIO_A.toarray()
        
        RMRIO_A = pd.DataFrame(RMRIO_A)
        
        # Add index
        
        RMRIO_A.index = pd.MultiIndex.from_frame(
            self.idx,
            )
        
        RMRIO_A.columns = pd.MultiIndex.from_frame(
            self.idx,
            )
        
        return RMRIO_A