# Exercitiul 1 (formula lui Bayes)

Să presupunem că investigăm o boală (B), care afectează doar un procent din populaţie $(P(B) = 0.01)$.
Avem un test de diagnosticare pentru această boală, care are următoarele caracteristici:
- **Sensibilitate** (probabilitatea ca testul să fie pozitiv dacă persoana este bolnavă): $P(Test = Pozitiv∣B) = 0.95$
- **Specificitate** (probabilitatea ca testul să fie negativ dacă persoana nu este bolnavă): $P(Test = Negativ∣¬B) = 0.90$

## Cerinta A 
Dacă o persoană este testată şi rezultatul este pozitiv, care este probabilitatea ca aceasta să fie efectiv bolnavă? Cum explicaţí rezultatul?

### Notatii

- $Poz: "Test=Pozitiv"$
- $Neg: "Test=Negativ"$

### Rezolvare

Practic, trebuie sa calculam $P(B|Poz)$.

Folosim formula lui Bayes: $P(B|Poz) = P(Poz|B)\cdot\frac{P(B)}{P(Poz)}$

Inlocuim valorile pe care le stim: $P(B|Poz) = 0.95 \cdot \frac {0.01}{P(Poz)}$

##### New Objective: $P(Poz)=?$

Ne folosim de **formula probabilitatii totale**:
- $P(Poz) = P(Poz \cap B) + P(Poz \cap \neg B)$

Inlocuim:
- $P(Poz) = P(Poz|B)\cdot P(B) + P(Poz|\neg B)\cdot P(\neg B)$

Inlocuim iar:
- $P(Poz) = 0.95 \cdot 0.01 + P(Poz|\neg B) \cdot P(\neg B)$

Stim ca:
- $P(Poz|\neg B)+P(Neg|\neg B) = 1$ (partitioneaza $\neg B$). Deci $P(Poz|\neg B) = 0.10$
- $P(\neg B) = 1-P(B) = 1 - 0.01 = 0.99$

Deci:
- $P(Poz) = 0.95 \cdot 0.01 + 0.10 \cdot 0.99 = 0.0095 + 0.099 = 0.1085$ (deci 10% din oameni vor testa pozitiv)

##### Revenind...
$P(B|Poz) = 0.95 \cdot \frac {0.01}{P(Poz)} = 0.95 \cdot \frac {0.01}{0.1085} = 0.0875576036... \approx 8.75\%$ (**Done! :)**)

## Cerinta B
Care ar trebui să fie specificitatea minimă pentru ca probabilitatea de mai sus să ajungă la 50%?
### Rezolvare
**Specificitate:** probabilitatea sa dea negativ la o persoana sanatoasa $P(Test = Negativ∣¬B)$
- Avem: $P(B|Poz) \ge 50\%$
- Cat este: $P(Test = Negativ∣¬B) = ?$

Inlocuind pe $P(B|Poz)$:
- $P(Poz|B)\cdot \frac {P(B)}{P(Poz)} \ge 50\%$

Inlocuim:
- $P(Poz)=P(Poz∣B)\cdot P(B)+P(Poz|\neg B)\cdot P(¬B)$
  
Stiind ca $P(Poz|\neg B)+P(Neg|\neg B) = 1$:
- $P(Poz) = P(Poz|B)\cdot P(B)+(1-P(Neg|\neg B))\cdot P(\neg B)$
- $P(Poz) = P(Poz|B)\cdot P(B)+(1-Specificitate)\cdot P(\neg B)$

Inlocuim in formula initiala:
- $P(Poz|B)\cdot \frac{P(B)}{P(Poz|B)\cdot P(B)+(1-Specificitate)\cdot P(\neg B)} \ge 50\%$
- $0.95 \cdot \frac {0.01}{0.95\cdot 0.01+(1-S)\cdot 0.99} \ge 0.5$
- $\frac {0.01}{0.95\cdot 0.01+(1-S)\cdot 0.99} \ge 0.526315...$
- $0.01\ge [0.95\cdot 0.01+(1-S)\cdot 0.99]\cdot 0.526315...$
- $0.019 \ge 0.95\cdot 0.01+(1-S)\cdot 0.99$
- $0.019 \ge 0.0095 + (1-S)\cdot 0.99$
- $0.0095 \ge 0.99\cdot (1-S)$
- $0.009595...\ge 1-S$
- $S+0.009595...\ge 1$
- $S\ge 0.990405$ (da, trebuie sa aiba specificitate mare pentru ca boala e foarte rara!)
  
**Done! :)**