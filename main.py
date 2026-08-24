from dataclasses import dataclass

@dataclass(frozen=True)
class Snapshot:
    project: str
    owner: str
    profile: str

def build_snapshot() -> Snapshot:
    return Snapshot("chat-queue-miaz", "CandaceRod47565", "0034")

if __name__ == "__main__":
    snapshot = build_snapshot()
    print(f"{snapshot.project}: {snapshot.owner}")
