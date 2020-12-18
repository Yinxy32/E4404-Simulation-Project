'''
Customer arrival simulation: nonhomogeneous poisson process
Customer arrival follows a nonhomogeneous poisson process for each day, and we know that customers are likely to purchase more orange in winter and purchase less in summer.  
lambda(t) = 30 * (-sin(2*pi*t/365) + 2)
Each arrival is willing to buy x units of orange, which follows a discrete uniform distribution 
U(0,  int(-price*0.05 + freshness*(50-price)/300))
'''
import numpy as np

def get_demand(a,b,c,inventory,freshness,random_state,d=0.05,e=50,f=300):
  '''
  a,b,c are parameters of the pricing formula.
  d,e,f are parameters of the demand curve
  '''
  price = linear_price(a,b,c,inventory,freshness)

  max_demand = np.ceil(-price*d + freshness*(e-price)/f)
  max_demand = max_demand*(max_demand>0)
  demand = random_state.randint(0,max_demand)
  return demand

def get_arrival(T=365,max_lm=90,random_state):
  '''
  Returns:
    np.array()
  '''
  t = 0

  inter_arrival=-1/max_lm*np.log(random_state.rand())
  t+=inter_arrival
  arrival_times=np.array([])
  while t<T:
      #check if the proposal is accepted or not
      if random_state.rand()<(max_lm/3*(-np.sin(2*np.pi*t/365) + 2))/max_lm:
        arrival_times=np.append(arrival_times,t)
      inter_arrival=-1/max_lm*np.log(random_state.rand())
      t+=inter_arrival

  return arrival_times
