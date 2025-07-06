import ingestion
import transformation
from storage import load
import missing_values_checking
import monitoring

if __name__ == "__main__":
    ingestion.main()
    transformation.main()
    load.main()
    missing_values_checking.monitor_data_missing_values()
    monitoring.compute_monitoring()
    print("[✓] Pipeline exécuté avec succès.")

