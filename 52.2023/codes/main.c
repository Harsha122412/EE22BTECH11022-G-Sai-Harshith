#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

double exponential(double lambda) {
    double U = (double)rand() / RAND_MAX;
    return -log(1 - U) / lambda;
}

int main() {
    double lambda = 1.0 / 2.0;
    double mu=2.0;
    int n_samples = 100000;
    int i;
    double sum_X = 0.0;
    double sum_Y = 0.0;
    int count_X_leq_mu = 0;
    int count_Y_leq_mu = 0;
    int count_X_geq_mu = 0;
    int count_Y_geq_mu = 0;
    srand(time(NULL));
    for (i = 0; i < n_samples; i++) {
        double X = exponential(lambda);
        double Y = floor(X);

        if (X <= mu) {
            count_X_leq_mu++;
        } else {
            count_X_geq_mu++;
        }

        if (Y <= mu) {
            count_Y_leq_mu++;
        } else {
            count_Y_geq_mu++;
        }

        sum_X += X;
        sum_Y += Y;
    }

    double pr_X_leq_mu = (double)count_X_leq_mu / n_samples;
    double pr_Y_leq_mu = (double)count_Y_leq_mu / n_samples;
    double pr_X_geq_mu = (double)count_X_geq_mu / n_samples;
    double pr_Y_geq_mu = (double)count_Y_geq_mu / n_samples;
    double E_X = sum_X / n_samples;
    double E_Y = sum_Y / n_samples;

    printf("Prob(X <= mu): %.5f\n", pr_X_leq_mu);
    printf("Prob(Y <= mu): %.5f\n", pr_Y_leq_mu);
    printf("Prob(X >= mu): %.5f\n", pr_X_geq_mu);
    printf("Prob(Y >= mu): %.5f\n", pr_Y_geq_mu);
    printf("E(X): %.5f\n", E_X);
    printf("E(Y): %.5f\n", E_Y);
    if(pr_Y_leq_mu <=  pr_X_leq_mu){
    	printf("P(Y <= mu)<=P(X <= mu), ");
    	printf("Option A correct\n");
    }
    else{
    	printf("P(Y <= mu)>=P(X <= mu), ");
    	printf("Option A wrong\n");
    }
    if(pr_Y_geq_mu <=  pr_X_geq_mu){
    	printf("P(Y >= mu)<=P(X >= mu), ");
    	printf("Option B correct\n");
    }
    else{
    	printf("P(Y >= mu)>=P(X >= mu), ");
    	printf("Option B wrong\n");
    }
    if(E_Y>E_X){
    	printf("E(Y)>E(X), ");
    	printf("Option C correct\n");
    }
    else{
    	printf("E(X)>E(Y), ");
    	printf("Option D correct\n");
    }
    return 0;
}
