
# raven_module.py
class Raven:
    name = "Raven"

    def evaluate_signals(self, state):
        alerts = []
        if state.get("pattern_shift_score", 0) > 0.6:
            alerts.append("Pattern drift detected — initiating deception audit.")
        if state.get("information_distortion", 0) > 0.5:
            alerts.append("False narrative vector rising — signal review needed.")
        return alerts
