import numpy as np
from scipy.stats import poisson, expon

# Parametrii inițiali
lambda_rate = 20  # numărul de clienți pe oră
mean_order_time = 2  # timpul mediu de plasare și plată a unei comenzi (minute)
prob_threshold = 0.95  # probabilitatea dorită de 95%
total_service_time_limit = 15  # limita de timp pentru a servi toți clienții într-o oră (minute)


# Funcția pentru a determina dacă un α dat satisface probabilitatea de 95%
def is_alpha_valid(alpha, num_simulations, lambda_rate, mean_order_time, total_service_time_limit, prob_threshold):
    numar_total_rulari = 0
    rulari_bune = 0
    for _ in range(num_simulations):
        num_clients = poisson.rvs(mu=lambda_rate)
        order_time_sum = np.sum(expon.rvs(scale=mean_order_time, size=num_clients))
        cooking_time_sum = np.sum(expon.rvs(scale=alpha, size=num_clients))
        total_time = order_time_sum + cooking_time_sum
        if total_time < total_service_time_limit * num_clients:
            rulari_bune += 1
        numar_total_rulari += 1
    prob = rulari_bune / numar_total_rulari
    return prob >= prob_threshold


# Căutarea lui α maxim
alpha_values = np.linspace(0.1, 5, 100)
alpha_max = None
print(is_alpha_valid(0.00001, 1000, lambda_rate, mean_order_time, total_service_time_limit, prob_threshold))
for alpha in alpha_values:
    if is_alpha_valid(alpha, 1000, lambda_rate, mean_order_time, total_service_time_limit, prob_threshold):
        alpha_max = alpha

# Afișarea rezultatului
print(f"Valoarea maximă a lui α: {alpha_max}")

# Calculul timpului mediu de așteptare pentru a fi servit al unui client
if alpha_max:
    waiting_times = [expon.rvs(scale=mean_order_time) + expon.rvs(scale=alpha_max) for _ in range(1000)]
    mean_waiting_time = np.mean(waiting_times)
    print(f"Timpul mediu de așteptare: {mean_waiting_time:.2f} minute")
