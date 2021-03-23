# How to Pandas

TBD: Flytt inn fra de andre arkene, både topp 10 og pandas generelt.

### Adjust output
`pd.set_option("display.precision", 3)` Use 3 decimal places in output display.  
`pd.set_option("display.expand_frame_repr", False)` Don't wrap repr(DataFrame) across additional lines.
`pd.set_option("display.max_rows", 25)` Set max rows displayed in output to 25.

### dtypes
`category` Nice, also reduces memory load.



### GroupBy
[GroupBy tutorial](https://realpython.com/pandas-groupby/)  

WIP - The Zen of Groupby:  
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


**Fra Pandas**  
`df.groupby(by=["col1"]).agg({"col2": "sum", "col3": lambda arr: myfunc(arr)})`  
`df = df.pivot_table(index=["id1", "id2"], columns="value_type_to_cols", values="Antall", aggfunc=np.sum, fill_value=0)` # Gen: Agg and reshape  
`df.groupby(col_or_any_list).agg(["mean"])` # By col or any right length list  

**Fra topp 10**
Split (into groups (Sers)) - apply (some function) - combine (to a data structure)  
`df.groupby(by=["col1"], as_index=False).agg("sum")` or a custom function  
`df.groupby(by=[df.index, "col1"]).agg({"col2": [np.min, np.size], "col3": cfunc})`  # Ser -> cfunc arg  
`df = df.pivot_table(index=["col1"], columns="Categories_as_Headers", values="Antall", aggfunc=np.sum, fill_value=0)` # Cat data as headers, aggr.  

Se the official documentation for [groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html?highlight=groupby#pandas.DataFrame.groupby)


## Time

### resampling TBD
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample
