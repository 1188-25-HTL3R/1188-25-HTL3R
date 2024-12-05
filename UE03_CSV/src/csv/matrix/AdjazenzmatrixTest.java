package csv.matrix;
import org.junit.Test;

import static csv.matrix.Adjazenzmatrix.*;
import static org.junit.Assert.assertArrayEquals;

public class AdjazenzmatrixTest {
    @Test
    public void adjazenzmatrix_test() {
        assertArrayEquals(
                new String[] {
                        "A: nach B:4, nach C:7, nach D:8",
                        "B: nach A:4, nach E:5, nach F:3",
                        "C: nach A:7, nach D:2, nach G:1",
                        "D: nach A:8, nach B:5, nach C:2, nach E:1, nach G:2",
                        "E: nach B:3, nach D:1, nach F:1, nach H:5",
                        "F: nach B:3, nach E:1, nach H:1",
                        "G: nach C:1, nach D:2, nach H:1",
                        "H: nach E:5, nach F:1, nach G:1"
                },
                printAdjazenzmatrix(getAdjazenzmatrix("src/csv/matrix/adjazenzmatrix.csv")));
    }


}
