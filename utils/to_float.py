def to_float(v):
        try:
            return float(v)
        except (ValueError, TypeError):
            return 0.0