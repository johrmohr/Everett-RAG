# Hugh Everett Typed description of Bayesian tracking filter.pdf

## EVERETT'S BAYSIAN FILTER  

A new approach for tracking maneuvering objects and for analysis of complex non- linear time series  

## BACKGROUND  

Almost all theoretical work in the fields of filter theory, time series analysis and tracking or trajectory prediction are based on the use of linear models. However, when the processes involved are very non- linear - - for example if distinct "turning points" can be expected in the data, or if the vehicle being tracked can execute even "optimism" deliberate maneuvers, then it has been found that the best possible linear filters systems produce far from satisfactory results. By definition, linear filters base their predictions of the future on some constant linear combination of past observations. Since such systems must attach constant weight to past observations (independent of the values encountered in more recent observations) the systems are inherently inefficient in recognizing turning points. If observations are smoothed over a sufficiently long time to permit good tracking and prediction of straight line segments, then the straight line trajectory will continue to be predicted well after a turn has occurred. If shorter smoothing constants are used, turns can be more efficiently recognized but the prediction accuracy for straight line segments is impaired. Consequently a considerable amount of practical work has been done on non- linear tracking and predictive systems that can adjust smoothing constants or use other tricks to respond more efficiently to turning points in the data. These non- linear systems tend to be based on heuristic concepts which make it difficult to assess the "efficiency" of the filters.

---

For example, when such a filter has been developed it is usually impossible to determine how close its performance approximates the best possible performance that could be obtained with a theoretically "optimum" or "perfect" non- linear filter. Most practical filter systems that are used to deal with non- linear processes fall into one of two categories  

1. Filter systems that can be shown to provide the "optimum" linear approximation for the non-linear process  

2. Non-linear filter systems based on heuristic concepts  

For processes that are very non- linear the first type of filter tends to be very inefficient, while the latter type is difficult to evaluate because of the absence of a theoretical basis of comparison which could show what could be accomplished with a theoretically perfect non- linear filter.  

Mathematicians involved in statistical decision theory have known for some time that a theoretical model of the "perfect" filter exists. This model is based on the use of an a- priori model of the dynamics of the process being observed, and the use of Baysian inference techniques to deduce the state of the system from the observations as the system evolves in time.  

While this basic theoretical concept is far from new, very little has been done to convert it into a practical computational procedure

---

## EVERETT'S CONCEPT  

The use of Baysian inference techniques in practical filter or tracking operations probably has not been exploited because of the tremendous computational burden that seems to be involved. For example, the a- priori Baysian distribution should include all possible initial states of the system, each with an appropriate weight. If the system is described by many parameters, then the dimensionality of the space of initial states can be immense. As the system evolves with time each of these states can branch stochastically into many other states. To carry out the Baysian if reference procedure, each of these states must be tested to determine how consistent it is with the observed measurements. Obviously this can imply an impossible data storage and computational burden.  

Everett's basic idea is to utilize statistical sampling techniques in order to make the calculations practical. Instead of using all possible system states for the prior distribution he utilizes an unbiased statistically selected sample of states. Each state is propagated forward in time according to the dynamical laws that govern system behavior. These laws may