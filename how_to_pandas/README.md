# How to Pandas

### Adjust output
`pd.set_option("display.precision", 3)` Use 3 decimal places in output display.  
`pd.set_option("display.expand_frame_repr", False)` Don't wrap repr(DataFrame) across additional lines.
`pd.set_option("display.max_rows", 25)` Set max rows displayed in output to 25.

### dtypes
`category` Nice, also reduces memory load.



### GroupBy
[GroupBy tutorial](https://realpython.com/pandas-groupby/)  



The Zen of Groupby:
Groupby uses the same **split-apply-combine** grouping as in SQL.   
**split**: Split the data into distinct bags based on some criteria. 
**apply**: Apply an aggregate function (like `sum` or `min`) to each bag. 
**combine**: Combine the aggregated bags into one table.


**df.groupby(by_what)[columns_to_aggregate].aggregate_function()**
* **by_what** - The crucial `by` argument and others.
  * `by` - The first argument, group by *what*?
    * Alt 1: Single `str` or `list` of `str` specifying *which columns* to group by.
    * Alt 2: A function, which will be run on the index.
    * Alt 3: A `dict` or Series. Not sure how they are being used.
  * `as_index` - by default, the groups labels will be returned in the index. If not, set `as_index=False` to use column(s) instead.
* **columns_to_aggregate** - a list of one or more columns to aggregate.
* **aggregate-function** - which function will be run on this. Typical examples are `count`, `min`, `max`, `mean`.


Se the official documentation for [groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html?highlight=groupby#pandas.DataFrame.groupby)


## Time

### resampling TBD
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample
