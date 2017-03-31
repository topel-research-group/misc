
args <- commandArgs(trailingOnly = TRUE)
mcmc<-read.table(args,header=T,skip=6)

# Illustrate standard deviation of split frequences in a graph.
tiff("StdDev.tiff", width=2400, height=2400, res = 300)
attach(mcmc)
#plot(mcmc$AvgStdDev.s., type="l",col="blue",xlab="Treesample")		# Or perhaps try "StdDev.s." instead.
#plot(mcmc[,30], type="l",col="blue",xlab="Treesample")
plot(mcmc[,78], type="l", col="blue", xlab="Treesample", ylab="AvgStdDev", yaxt = "n")
axis(2, at=c(0.25, 0.2, 0.15, 0.1, 0.05, 0.01), labels=c("0.25", "0.2", "0.15", "0.1", "0.05", "0.01"))
abline(.01,0)


# Plot misc. mixing statistics from the MrBayes analysis.
tiff("misc_mcmc.tiff", width=2400, height=2400, res = 200)
par(mfrow=c(4,5))
for (i in 2:11){
plot(mcmc[,1],mcmc[,i],main=names(mcmc[i]),type="l",col="red")
}
for (i in 18:27){
plot(mcmc[,1],mcmc[,i],main=names(mcmc[i]),type="l",col="red")
}

# Plot mixing between chains
tiff("mixing.tiff", width=2400, height=2400, res = 200)
par(mfrow=c(2,6))
for (i in 12:17){
plot(mcmc[,1],mcmc[,i],main=names(mcmc[i]),type="l",col="red")
}
for (i in 28:33){
plot(mcmc[,1],mcmc[,i],main=names(mcmc[i]),type="l",col="red")
}
