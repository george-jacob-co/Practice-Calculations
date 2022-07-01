def savings(gross_pay, tax_rate, expenses):
    return (int(gross_pay*(1-float(tax_rate)))-int(expenses))

def material_waste(total_material, material_units, num_jobs, job_consumption):
    return(str((total_material-(num_jobs*job_consumption)))+str(material_units))

def interest(principal, rate, periods):
    return(int(principal*(float(rate)*periods)+principal))

def body_mass_index(weight, height):
    kg = float(weight)/2.2046
    ft,inches = height.split("'")
    m = (int(ft)/3.281) + int(inches.strip('"'))/39.37
    return float(kg/(m ** 2))

