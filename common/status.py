from enum import StrEnum

class SimulationStatus(StrEnum):
    created = "created"
    setup_running = "setup_running"
    setup_done = "setup_done"
    setup_failed = "setup_failed"

    queued = "queued"
    dssat_running = "dssat_running"
    dssat_done = "dssat_done"
    dssat_failed = "dssat_failed"

    optimization_running = "optimization_running"
    optimization_done = "optimization_done"
    optimization_failed = "optimization_failed"

    finalize_running = "finalize_running"
    finalize_done = "finalize_done"
    finalize_failed = "finalize_failed"

    finished = "finished"

