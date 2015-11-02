///
/// System : JPortal
/// $Source: /main/nedcor/cvsroot/dev/jportal/Query.java,v $
/// $Author: vince $
/// $Date: 2002/03/13 11:57:19 $
/// $Revision: 1.3 $
///

package vlab.crackle.rpc;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class Query
{
  public PreparedStatement prep;
  public ResultSet result;
  public Query(PreparedStatement prep, ResultSet result)
  {
    this.prep = prep;
    this.result = result;
  }
  public void close() throws SQLException
  {
    result.close();
    prep.close();
  }
}
