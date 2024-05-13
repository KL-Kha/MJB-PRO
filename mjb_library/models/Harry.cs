createRecord(
    timestamp,
    orderId,
    [
        {
            'type': 'LOGS',
            'value': 'results.txt'
        },
        {
            'type': 'DEVUI',
            'value': '123456789'
        },
        {
            'type': 'MAC',
            'value': 'sfds234:12313fdsff'
        }
    ]
)

// every 5s
var todo = readQueue()
if todo:
    startProgram(todo)


// Step 1:
// Read the order data from MES = you get the order id + all the attributes
// SELECT 
//     x_mes_order.*,
//     x_mes_attribute.* 
// FROM x_mes_order 
// WHERE orderID = interfaceID
// LEFT INNER JOIN x_mes_attribute on x_mes_attribute.orderID = interfaceID

// Step 2: 
// Run your program 
// Create record in MES for results

// Create a new record in MES
// uniqueKey = must be a unique uid for the record
// orderId = must be a MES ORDER ID (need to read first)
// inputs = array of values
function createRecord(uniqueKey='', orderId=123, inputs=[])
{
    string connectionString = "Server=mes.majorbird.cn;port=5434;Username=odo0re;Password=od!fFDs09812;Database=MES_MAJORBIRD";
    // Making connection with Npgsql provider
    var conn = new NpgsqlConnection(connectionString);
    conn.Open();
    var cmd = new NpgsqlCommand();
    cmd.Connection = conn;

    data = [
        (uniqueKey,'LOGS', 'test.txt')
        (uniqueKey,'START', 'test.txt')
        (uniqueKey,'END', 'test.txt')
        (uniqueKey,'BADGE_ID', 'test.txt')
        (uniqueKey,'DEVUI', 'test.txt')
    ]

    cmd.CommandText = @"INSERT INTO x_mes_data (x_name,x_type,x_value) VALUES data";
    cmd.Parameters.AddWithValue("t", PC_numberbox.Text.ToString());
    cmd.Parameters.AddWithValue("v", PC_numberbox.Text.ToString());
    cmd.Parameters.AddWithValue("p", PC_numberbox.Text.ToString());
    cmd.ExecuteNonQuery();
}