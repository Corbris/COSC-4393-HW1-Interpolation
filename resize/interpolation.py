class interpolation:

    def linear_interpolation(self, pt1, pt2, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        #Write your code for linear interpolation here

        if pt1[1] != pt2[1]: #horizontal
            P = ((pt2[1] - unknown[1]) / (pt2[1] - pt1[1])) * pt1[2] + ((unknown[1] - pt1[1]) / (pt2[1] - pt1[1])) * pt2[2]
        else: #vertical
            P = ((pt1[0] - unknown[0]) / (pt1[0] - pt2[0])) * pt2[2] + ((unknown[0] - pt2[0]) / (pt1[0] - pt2[0])) * pt1[2]

        return P

    def bilinear_interpolation(self, pt1, pt2, pt3, pt4, unknown):
        """Computes the linear interpolation for the unknown values using pt1 and pt2
        take as input
        pt1: known point pt1 and f(pt1) or intensity value
        pt2: known point pt2 and f(pt2) or intensity value
        pt1: known point pt3 and f(pt3) or intensity value
        pt2: known point pt4 and f(pt4) or intensity value
        unknown: take and unknown location
        return the f(unknown) or intentity at unknown"""

        # Write your code for bilinear interpolation here
        # May be you can reuse or call linear interpolatio method to compute this task

        R1 = self.linear_interpolation(pt3, pt4, unknown)  #Bot row horizontal
        R2 = self.linear_interpolation(pt1, pt2, unknown)  #Top row Horizontal

        vert1 = [pt1[0], unknown[1], R2]  #top point       #point for R2(top)
        vert2 = [pt3[0], unknown[1], R1]  #bot point       #point for R1(bot)

        P = self.linear_interpolation(vert1, vert2, unknown) #P vertical

        return P

