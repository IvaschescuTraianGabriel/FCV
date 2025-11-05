from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict, Any

@dataclass
class OperationConfig:
    name: str
    params: Dict[str, Any]


# A PipelineConfig is a list of operations to apply sequentially
PipelineConfig = List[OperationConfig]


def _parse_value(value: str):
    """
    Try to parse into int/float/bool, otherwise keep string.
    """
    v = value.strip()
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    # int?
    try:
        return int(v)
    except ValueError:
        pass
    # float?
    try:
        return float(v)
    except ValueError:
        pass
    return v


def load_config(path: Path) -> List[PipelineConfig]:
    """
    Load pipeline configurations from a plain text file.
    Syntax:
        # comment
        dummy
        brightness_manual delta=30
        contrast alpha=1.2 beta=0 | resize scale=0.5
    """
    pipelines: List[PipelineConfig] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # Split chain by '|'
            op_specs = [seg.strip() for seg in line.split("|") if seg.strip()]
            ops: PipelineConfig = []

            for spec in op_specs:
                tokens = spec.split()
                if not tokens:
                    continue
                name = tokens[0]
                params: Dict[str, Any] = {}
                for tok in tokens[1:]:
                    if "=" in tok:
                        key, val = tok.split("=", 1)
                        params[key.strip()] = _parse_value(val)
                ops.append(OperationConfig(name=name, params=params))

            if ops:
                pipelines.append(ops)

    return pipelines
