#include <stdio.h>
#include <math.h>

#define N 100

int main() {
    double mu_values[N];
    double cdf_X[N];
    double cdf_Y[N];
    int i;
    for (i = 0; i < N; i++) {
        mu_values[i] = 1 + (4.0 * i) / (N - 1);
    }
    FILE *file = fopen("cdf_values.dat", "w");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }
    fprintf(file, "mu\tcdf_X\tcdf_Y\n");
    for (i = 0; i < N; i++) {
        double mu = mu_values[i];
        cdf_X[i] = 1 - exp(-1.5 / mu);
        cdf_Y[i] = 1 - exp(-floor(1.5) / mu); 
        fprintf(file, "%.2lf\t%.6lf\t%.6lf\n", mu, cdf_X[i], cdf_Y[i]);
    }
    fclose(file);
    return 0;
}

