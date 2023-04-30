"""
This program implements a function to calculate the dosage to paracetamol

Project No.Name: 3.8.3_ Paracetamol Dosage
Name: Mijanur Rahman (mijanur.m.rahman@tuni.fi)
Student ID: 151762776
"""


def calculate_dose(patient_weight, time_lapsed_till_last_dose,
                   dosage_in_24_hours):
    """
    This function calculates the dosage of paracetamol based on the
    given parameters
    :param patient_weight:
    :param time_lapsed_till_last_dose:
    :param dosage_in_24_hours:
    :return:
    """
    dosage_safe_window = 6
    dose_per_kg = 15
    max_daily_dose = 4000

    if time_lapsed_till_last_dose >= dosage_safe_window:
        if dosage_in_24_hours < max_daily_dose:
            if (dose_per_kg * patient_weight) >= (max_daily_dose - dosage_in_24_hours):
                return max_daily_dose - dosage_in_24_hours
            else:
                return dose_per_kg * patient_weight
        else:
            return 0
    else:
        return 0


def main():
    weight = int(input("Patient's weight (kg): "))
    time_lapsed = int(input("How much time has passed from the previous dose (full hours): "))
    dosage_24_hours = int(input("The total dose for the last 24 hours (mg): "))

    print(f"The amount of Parasetamol to give to the patient: "
          f"{calculate_dose(weight, time_lapsed, dosage_24_hours)}")


if __name__ == "__main__":
    main()
