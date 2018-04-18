import pandas as pd

class HodoSummary:
    def __init__(self, filename):
        self.headers = [
            "sector", 
            "layer", 
            "component",
            "m_noise_charge", 
            "m_noise_maxV",
            "m_mips_charge",
            "m_mips_maxV",
            "m_tiles_charge",
            "m_tiles_maxV",
            "e_noise_charge", 
            "e_noise_maxV",
            "e_mips_charge",
            "e_mips_maxV",
            "e_tiles_charge",
            "e_tiles_maxV",
        ]
        self.sectors = range(1,9)
        self.layers = range(1,3)
        self.filename = filename
        self.df = pd.read_csv(self.filename, delim_whitespace=True, names=self.headers)
        
    def get_sector_data(self, sector, layer, value):
        data = self.df[(self.df['sector']==sector) & (self.df['layer']==layer)]
        return data['component'].values, data[value].values, data['e'+ value[1:]]
    
    def get_data_flat(self, value):
        return self.df[value].values
        


class HodoSummarySet:
    def __init__(self):
        self.headers = [
            "sector", 
            "layer", 
            "component",
            "m_noise_charge", 
            "m_noise_maxV",
            "m_mips_charge",
            "m_mips_maxV",
            "m_tiles_charge",
            "m_tiles_maxV",
            "e_noise_charge", 
            "e_noise_maxV",
            "e_mips_charge",
            "e_mips_maxV",
            "e_tiles_charge",
            "e_tiles_maxV",
            "run_id",
        ]
        self.sectors = range(1,9)
        self.layers = range(1,3)
        self.runs = []
        self.df = pd.DataFrame(columns=self.headers)
        
    def load_summary_file(self, filename, run_id):
        df_temp = pd.read_csv(filename, delim_whitespace=True, names=self.headers)
        df_temp['run_id'] = run_id
        self.df = pd.concat([self.df, df_temp], ignore_index=True)
        self.runs.append(run_id)
        
    def get_sector_data(self, run_id, sector, layer, value):
        data = self.df[(self.df['run_id']==run_id) & 
                       (self.df['sector']==sector) & 
                       (self.df['layer']==layer)]
        return data['component'].values, data[value].values, data['e'+ value[1:]].values
